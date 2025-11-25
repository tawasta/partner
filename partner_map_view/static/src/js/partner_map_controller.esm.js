/** @odoo-module */

import {
    Component,
    onMounted,
    onWillStart,
    onWillUpdateProps,
} from "@odoo/owl";
import {Layout} from "@web/search/layout";
import {SearchBar} from "@web/search/search_bar/search_bar";
import {useService} from "@web/core/utils/hooks";

export class PartnerMapController extends Component {
    setup() {
        this.orm = useService("orm");
        this.rpc = useService("rpc");
        this.model = useState(
            new this.props.Model(
                this.orm,
                this.rpc,
                this.props.resModel,
                this.env.searchModel,
                this.props.fields,
                this.props.archInfo,
                this.props.domain
            )
        );
        onMounted(async () => {
            await this.model.load();
        });

        onWillStart(async () => {
            await this.model.load();
        });

        onWillUpdateProps(async () => {
            await this.model.load();
        });
    }
}

PartnerMapController.components = {Layout, SearchBar};
PartnerMapController.template = "partner_map_view.View";
