/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import {jsonrpc} from "@web/core/network/rpc_service";

/**
 * PartnerDomainChecker
 *
 * Tämä widget tarkistaa, kuuluuko käyttäjän partner tiettyyn partner domainiin.
 * Jos ehto täyttyy, lisätään domainin nimi <html>-elementin datasettiin (data-partner-domain).
 *
 * Käyttö:
 * Lisää mihin tahansa elementtiin attribuutti:
 *   data-visibility-value-partner-domain='[{"id": <filter_id>, "name": "<nimi>"}]'
 *
 * Widget kutsuu backend-endpointia /website/partner_domain_check ja päivittää
 * HTML-datasetin sen mukaan.
 */
const PartnerDomainChecker = publicWidget.Widget.extend({
    selector: "[data-visibility-value-partner-domain]",

    /**
     * Start() ajetaan automaattisesti kun widget alustetaan DOM-elementille.
     */
    async start() {
        await this._super(...arguments);

        const htmlEl = document.documentElement;
        const filters = JSON.parse(
            this.el.dataset.visibilityValuePartnerDomain || "[]"
        );

        console.log("PartnerDomainChecker: Löydetyt filterit:", filters);

        for (const f of filters) {
            if (!f.id) {
                continue; // Jos filterillä ei ole id:tä, ohitetaan
            }

            try {
                console.log("PartnerDomainChecker: Tarkistetaan filter_id=", f.id);
                // Pyydetään serveriltä tieto, täsmääkö partner nykykäyttäjään
                const res = await jsonrpc("/website/partner_domain_check", {
                    filter_id: f.id,
                });
                console.log("PartnerDomainChecker: Serveriltä saatu vastaus:", res);

                // Jos ehto täyttyy, tallennetaan domainin nimi datasettiin
                if (res.matched) {
                    const existing = htmlEl.dataset.partnerDomain || "";
                    htmlEl.dataset.partnerDomain = existing
                        ? `${existing},${res.name}`
                        : res.name;

                    console.log(
                        "PartnerDomainChecker: Match löytyi! Lisättiin datasettiin:",
                        htmlEl.dataset.partnerDomain
                    );
                }
            } catch (e) {
                console.error("Partner domain check failed", e);
            }
        }
    },
});

// Rekisteröidään widget julkiselle puolelle
publicWidget.registry.partner_domain_checker = PartnerDomainChecker;

export {PartnerDomainChecker};
