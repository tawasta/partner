/** @odoo-module */

import {Layout} from "@web/search/layout";
import {SearchBar} from "@web/search/search_bar/search_bar";
import {useService} from "@web/core/utils/hooks";
import {Component, onWillStart, useState} from "@odoo/owl";

export class PartnerMapController extends Component {
    static components = {Layout, SearchBar};
    static template = "partner_map_view.View";
    setup() {
        this.orm = useService("orm");
        this.rpc = useService("rpc");
        this.model = useState(
            new this.props.Model(
                this.orm,
                this.rpc,
                this.props.resModel,
                this.props.fields,
                this.props.archInfo,
                this.props.domain
            )
        );

        onWillStart(async () => {

            await this.model.load();
        });
    }
}
