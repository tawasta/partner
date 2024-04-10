from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(
        env,
        [
            ("res.partner", "res_partner", "guardians", "guardian_ids"),
            ("res.partner", "res_partner", "wards", "ward_ids"),
        ],
    )
