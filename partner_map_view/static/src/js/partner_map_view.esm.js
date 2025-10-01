/** @odoo-module */

import {PartnerMapArchParser} from "./partner_map_arch_parser";
import {PartnerMapController} from "./partner_map_controller";
import {PartnerMapModel} from "./partner_map_model";
import {registry} from "@web/core/registry";
import {PartnerMapRenderer} from "./partner_map_renderer";

export const partnerMapView = {
    type: "partnerMapView",
    display_name: "Map",
    icon: "fa fa-picture-o",
    multiRecord: true,
    Controller: PartnerMapController,
    ArchParser: PartnerMapArchParser,
    Model: PartnerMapModel,
    Renderer: PartnerMapRenderer,

    props(genericProps, view) {
        const {ArchParser} = view;
        const {arch} = genericProps;
        const archInfo = new ArchParser().parse(arch);

        return {
            ...genericProps,
            Model: view.Model,
            Renderer: view.Renderer,
            archInfo,
        };
    },
};

registry.category("views").add("partnerMapView", partnerMapView);
