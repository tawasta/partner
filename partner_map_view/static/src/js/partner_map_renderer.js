/** @odoo-module */

import { Component, onMounted } from "@odoo/owl";

export class PartnerMapRenderer extends Component {
    setup() {
        onMounted(async () => {
            this.map = L.map('partner_map').setView([this.props.company_location.latitude, this.props.company_location.longitude], 13);
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(this.map);
            this.props.records.forEach((record) => {
                L.marker([record.latitude, record.longitude]).bindPopup(record.text).addTo(this.map);
            });
        });
    }
}

PartnerMapRenderer.template = "partner_map_view.Renderer";
