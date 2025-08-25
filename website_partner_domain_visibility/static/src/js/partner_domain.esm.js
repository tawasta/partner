/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import {jsonrpc} from "@web/core/network/rpc_service";

/**
 * PartnerDomainChecker
 *
 * Tämä widget tarkistaa, kuuluuko käyttäjän partner tiettyyn partner domainiin.
 * Jos ehto täyttyy, lisätään domainin nimi sekä blokin datasettiin että globaalisti <html>-elementin datasettiin.
 *
 * Käyttö:
 * Lisää mihin tahansa elementtiin attribuutti:
 *   data-visibility-value-partner-domain='[{"id": <filter_id>, "name": "<nimi>"}]'
 */
const PartnerDomainChecker = publicWidget.Widget.extend({
    selector: "[data-visibility-value-partner-domain]",

    async start() {
        await this._super(...arguments);

        const htmlEl = document.documentElement;
        const filters = JSON.parse(
            this.el.dataset.visibilityValuePartnerDomain || "[]"
        );

        console.log(
            "PartnerDomainChecker: Löydetyt filterit:",
            filters,
            "elementissä",
            this.el
        );

        for (const f of filters) {
            if (!f.id) continue;

            try {
                console.log("PartnerDomainChecker: Tarkistetaan filter_id=", f.id);
                const res = await jsonrpc("/website/partner_domain_check", {
                    filter_id: f.id,
                });
                console.log("PartnerDomainChecker: Serveriltä saatu vastaus:", res);

                if (res.matched) {
                    // 1. Kirjoitetaan suoraan tälle blokille
                    this.el.dataset.partnerDomain = res.name;

                    // 2. Päivitetään myös globaali <html>-attribuutti (jos halutaan CSS-tyylittelyyn)
                    const existing = htmlEl.dataset.partnerDomain || "";
                    htmlEl.dataset.partnerDomain = existing
                        ? `${existing},${res.name}`
                        : res.name;

                    console.log(
                        "PartnerDomainChecker: Match löytyi! Blokki sai datasetin:",
                        this.el,
                        "->",
                        this.el.dataset.partnerDomain,
                        "| html.dataset.partnerDomain:",
                        htmlEl.dataset.partnerDomain
                    );
                }
            } catch (e) {
                console.error("PartnerDomainChecker: Server-kutsu epäonnistui", e);
            }
        }
    },
});

publicWidget.registry.partner_domain_checker = PartnerDomainChecker;

export {PartnerDomainChecker};
