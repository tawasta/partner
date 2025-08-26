/** @odoo-module **/

/*
 * PartnerDomainController
 *
 * Mitä tämä tekee, lyhyesti ja yleistajuisesti:
 * - Sivulla on sisältölohkoja (elementtejä), joihin on liitetty "filttereitä".
 * - Jokainen filtteri kysyy palvelimelta (RPC), kuuluuko kävijä tiettyyn ryhmään
 *   (esim. kumppani/asiakas-segmentti) domainin perusteella.
 * - Jos jokin filtteri täsmää, elementti näytetään väkisin näkyvissä (ilman että
 *   rikotaan sivunrakentajan omia tunnisteita). Jos mikään ei täsmää, elementti
 *   jätetään sivunrakentajan hallittavaksi (eli se voi olla piilotettu).
 *
 * Tärkeää:
 * - Emme muuta pysyvästi sivua; näkyvyys tehdään vain tämän sivulatauksen ajaksi.
 * - Emme koske builderin data-visibility-id -arvoon.
 * - Yhden sivun sisällä käsittelemme elementit jonossa, jotta järjestys pysyy siistinä.
 */

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

/* ==================== Pienet apurit ==================== */

/** Siistii nimen/otsikon: poistaa turhat välilyönnit. */
function normalizeToken(token) {
    return String(token ?? "").replace(/\s+/g, " ").trim();
}

/** Odota seuraava selainpiirto (auttaa, että CSS päivittyy). */
function nextFrame() {
    return new Promise((res) => requestAnimationFrame(() => res()));
}

/** Odota pari piirtoa, jotta näkyvyys ehtii asettua. */
async function settleFrames(times = 2) {
    for (let i = 0; i < times; i++) await nextFrame();
}

/** Palauttaa elementin takaisin builderin hallintaan (poistaa meidän pakotukset). */
function resetElementState(el) {
    const wasForced = el.getAttribute("data-pdc-forced-display") === "1";
    const removedInvisible = el.getAttribute("data-pdc-removed-invisible") === "1";

    // Poista meidän asettama inline-näkyvyys
    if (wasForced) {
        el.style.removeProperty("display");
        el.removeAttribute("data-pdc-forced-display");
    }
    // Jos poistimme aiemmin builderin "näkymätön"-luokan, palauta se
    if (removedInvisible) {
        el.classList.add("o_snippet_invisible");
        el.removeAttribute("data-pdc-removed-invisible");
    }

    // Siivotaan meiltä jääneet tunnisteet
    if (el.hasAttribute("data-partner-domain")) {
        el.removeAttribute("data-partner-domain");
    }
    if (el.hasAttribute("data-visibility-id-original")) {
        el.removeAttribute("data-visibility-id-original");
    }
}

/** Pakota elementti näkyviin koskematta builderin omiin tunnisteisiin. */
function forceVisible(el) {
    if (el.classList.contains("o_snippet_invisible")) {
        // Jos builder oli merkinnyt lohkon näkymättömäksi, kumoamme sen väliaikaisesti
        el.classList.remove("o_snippet_invisible");
        el.setAttribute("data-pdc-removed-invisible", "1");
    }
    // Näytä lohko varmasti
    el.style.setProperty("display", "block", "important");
    el.setAttribute("data-pdc-forced-display", "1");
}

/* ==================== Yksinkertainen "sarjajono" koko sivulle ==================== */
/* Varmistaa, että käsittelemme elementit siistissä järjestyksessä, yksi kerrallaan. */
const QUEUE_KEY = "__pdcQueue";
if (!window[QUEUE_KEY]) window[QUEUE_KEY] = Promise.resolve();
function runSerial(taskFn) {
    const chain = window[QUEUE_KEY].then(taskFn, taskFn);
    window[QUEUE_KEY] = chain.catch(() => {});
    return chain;
}

/* ==================== Varsinainen widget ==================== */
const PartnerDomainController = publicWidget.Widget.extend({
    // Ajetaan koko sivun pääkääreen alla
    selector: "#wrap",

    init() {
        this._super(...arguments);
        this._ran = false; // Estetään turha tuplasuoritus
    },

    async start() {
        await this._super(...arguments);

        // Haluamme ajaa tämän vain kerran sivulatausta kohti
        if (this._ran) return;
        this._ran = true;

        const htmlEl = document.documentElement;
        const nodes = Array.from(
            document.querySelectorAll("[data-visibility-value-partner-domain]")
        );

        // Käydään läpi kaikki kohteet peräkkäin (jotta muutosjärjestys on selkeä)
        for (let idx = 0; idx < nodes.length; idx++) {
            await runSerial(async () => {
                const el = nodes[idx];

                // 0) Siivoa mahdolliset aiemmat pakotukset ennen uutta tarkastusta
                resetElementState(el);

                // 1) Lue elementtiin määritellyt filtterit (JSON-array attribuutissa)
                let filters = [];
                try {
                    const raw = el.getAttribute("data-visibility-value-partner-domain") || "[]";
                    const parsed = JSON.parse(raw);
                    filters = Array.isArray(parsed) ? parsed : [];
                } catch {
                    // Viallinen JSON -> tulkitaan ettei filttereitä ole
                    filters = [];
                }

                let shown = false;

                // 2) Kokeile filttereitä järjestyksessä, ensimmäinen osuma riittää
                for (let i = 0; i < filters.length; i++) {
                    const f = filters[i];
                    if (!f || !f.id) continue;

                    try {
                        // Kysytään palvelimelta, täsmääkö tämä filtteri kävijään
                        const res = await jsonrpc("/website/partner_domain_check", { filter_id: f.id });

                        const matched = !!(res && res.matched);
                        const name = normalizeToken(res && res.name);

                        if (!matched || !name) continue;

                        // Kirjataan nimi elementtiin (helpottaa esim. testauksessa/tyyleissä)
                        el.setAttribute("data-partner-domain", name);

                        // Näytetään elementti varmasti
                        forceVisible(el);

                        // Asetetaan hetkeksi sama nimi myös <html>-tasolle,
                        // jotta builderin mahdolliset säännöt osaavat toimia.
                        // Poistamme tämän myöhemmin, ettei jää pysyväksi.
                        htmlEl.setAttribute("data-partner-domain", name);

                        // Odota hetki, että selaimen tyylit ehtivät päivittyä
                        await settleFrames(1);

                        shown = true;
                        break; // ensimmäinen täsmäys riittää
                    } catch {
                        // Palvelinkutsu epäonnistui -> ohitetaan tämä filtteri hiljaisesti
                    }
                }

                // 3) Jos mikään filtteri ei täsmännyt, palautetaan elementti builderin hallintaan
                if (!shown) {
                    resetElementState(el);
                    el.removeAttribute("data-partner-domain");
                }

                // 4) Siivoa <html>-tason väliaikainen attribuutti
                htmlEl.removeAttribute("data-partner-domain");
            });
        }
    },
});

publicWidget.registry.partner_domain_checker = PartnerDomainController;

export { PartnerDomainController };
