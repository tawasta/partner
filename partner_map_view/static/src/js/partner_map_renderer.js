/** @odoo-module */

import {Component, onMounted} from "@odoo/owl";

export class PartnerMapRenderer extends Component {
    static template = "partner_map_view.Renderer";
    setup() {
        onMounted(async () => {
            this.map = L.map("partner_map").setView(
                [
                    this.props.company_location.latitude,
                    this.props.company_location.longitude,
                ],
                13
            );
            L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
                maxZoom: 19,
                attribution: "&copy; <a href=\"http://www.openstreetmap.org/copyright\">OpenStreetMap</a>"
            }).addTo(this.map);
            this.props.records.forEach((record) => {
                let text =
                    record.text +
                    " <a href='https://www.google.com/maps?z=15&q=" +
                    record.latitude +
                    "," +
                    record.longitude +
                    "' target='_blank'>Google Maps</a>";
                L.marker([record.latitude, record.longitude])
                    .bindPopup(text)
                    .addTo(this.map);
            });
        });
    }
}
