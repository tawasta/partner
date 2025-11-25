/** @odoo-module */

export class PartnerMapArchParser {
    parse(arch) {
        const text = arch.getAttribute("text");
        return {
            text,
        };
    }
}
