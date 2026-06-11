/** @odoo-module **/

import {patch} from "@web/core/utils/patch";
import {FormController} from "@web/views/form/form_controller";
import {ConfirmationDialog} from "@web/core/confirmation_dialog/confirmation_dialog";
import {_t} from "@web/core/l10n/translation";

patch(FormController.prototype, {
    async saveButtonClicked(params = {}) {
        const record = this.model.root;

        if (
            record &&
            record.resModel === "res.partner" &&
            !record.resId &&
            !this._factoringReminderConfirmed
        ) {
            this._factoringReminderConfirmed = true;

            this.dialogService.add(ConfirmationDialog, {
                title: _t("Factoring-muistutus"),
                body: _t("Muistithan tarkistaa Factoringin?"),
                confirmLabel: _t("Jatka tallennusta"),
                cancelLabel: _t("Palaa tarkistamaan"),
                confirm: async () => {
                    await this.saveButtonClicked(params);
                },
                cancel: () => {
                    this._factoringReminderConfirmed = false;
                },
            });

            return false;
        }

        return await super.saveButtonClicked(params);
    },
});
