/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import {jsonrpc} from "@web/core/network/rpc_service";

const PartnerDomainChecker = publicWidget.Widget.extend({
    selector: "[data-visibility-value-partner-domain]",

    async start() {
        await this._super(...arguments);

        const htmlEl = document.documentElement;
        const filters = JSON.parse(
            this.el.dataset.visibilityValuePartnerDomain || "[]"
        );

        // Käydään filterit läpi järjestyksessä, yksi kerrallaan
        for (let i = 0; i < filters.length; i++) {
            const f = filters[i];
            if (!f.id) continue;

            try {
                // Odotetaan vastausta ennen seuraavaan siirtymistä
                const res = await jsonrpc("/website/partner_domain_check", {
                    filter_id: f.id,
                });

                if (res.matched) {
                    // 1. Kirjoitetaan suoraan tälle blokille
                    this.el.dataset.partnerDomain = res.name;

                    // 2. Päivitetään globaali <html>-attribuutti ilman duplikaatteja
                    const existing = htmlEl.dataset.partnerDomain
                        ? htmlEl.dataset.partnerDomain.split(",")
                        : [];
                    if (!existing.includes(res.name)) {
                        existing.push(res.name);
                    }
                    htmlEl.dataset.partnerDomain = existing.join(",");
                }
            } catch (e) {
                console.error("PartnerDomainChecker: Server-kutsu epäonnistui", e);
            }
        }
    },
});

publicWidget.registry.partner_domain_checker = PartnerDomainChecker;

export {PartnerDomainChecker};
