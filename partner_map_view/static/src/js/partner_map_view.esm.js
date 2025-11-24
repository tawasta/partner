/** @odoo-module */

import {PartnerMapArchParser} from "./partner_map_arch_parser.esm";
import {PartnerMapController} from "./partner_map_controller.esm";
import {PartnerMapModel} from "./partner_map_model.esm";
import {PartnerMapRenderer} from "./partner_map_renderer.esm";
import {registry} from "@web/core/registry";

export const partnerMapView = {
    type: "partnerMapView",
    display_name: "Map",
    icon: "fa fa-map",
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
