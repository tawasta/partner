import calendar
import logging
from datetime import date

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    date_range_ids = fields.One2many(
        "res.partner.date.range", "partner_id", string="Date Range Based Infos"
    )

    def check_date_ranges_exist(self, date_range_type_code):
        """
        Helper function other modules can call for checking that specific
        type of entries exist in the first place.
        """

        self.ensure_one()

        ranges = self.date_range_ids.filtered(
            lambda r: r.type_id and r.type_id.code == date_range_type_code
        )

        return len(ranges) > 0

    def check_date_range_for_match(self, date_range_type_code, date_target):
        """
        Helper function other modules can call with e.g.
        check_date_range_for_match("BOARD_MEMBER", <date object>)
        to see if there is a entry for the partner for a particular code for that date.
        """

        self.ensure_one()

        ranges = self.date_range_ids.filtered(
            lambda r: r.type_id and r.type_id.code == date_range_type_code
        )

        for r in ranges:
            start_ok = not r.date_start or date_target >= r.date_start
            end_ok = not r.date_end or date_target <= r.date_end
            if start_ok and end_ok:
                return True

        return False

    def check_year_for_covered_months(
        self, date_range_type_code, year_target, full_months_only=True
    ):
        """
        Helper function other modules can call to count
        how many months (0-12) in year_target are covered by this partner's
        date ranges that match a particular type code.

        Use e.g. if certain price/perk is relevant for a year,
        if more than 6 months of that year are covered.

        - date_range_type_code: string code to filter date.range.type
          (e.g. "BOARD_MEMBER")
        - year_target: int (e.g. 2025)
        - full_months_only: True => month counts only if every day of the month is
                                    covered
                            False => any overlap with the month counts

        Returns an int between 0 and 12.
        """
        self.ensure_one()

        year = int(year_target)

        # prepare the ranges that match the asked type code
        ranges = []
        for r in self.date_range_ids:
            if not r.type_id or r.type_id.code != date_range_type_code:
                continue
            start = r.date_start or date.min
            end = r.date_end or date.max
            if start > end:
                # skip invalid ranges
                continue
            ranges.append((start, end))

        if not ranges:
            return 0

        covered_months = 0

        for month in range(1, 13):
            month_start = date(year, month, 1)
            month_last_day = calendar.monthrange(year, month)[1]
            month_end = date(year, month, month_last_day)

            if not full_months_only:
                # any overlap with the month counts
                overlaps = any(
                    (start <= month_end and end >= month_start) for start, end in ranges
                )
                if overlaps:
                    covered_months += 1
                continue

            # for full months only logic: compute total covered days in this month
            # across ranges
            days_in_month = month_last_day
            days_covered = 0
            for start, end in ranges:
                # overlap between [start,end] and [month_start,month_end]
                overlap_start = start if start > month_start else month_start
                overlap_end = end if end < month_end else month_end
                if overlap_start <= overlap_end:
                    days_covered += (overlap_end - overlap_start).days + 1
                    if days_covered >= days_in_month:
                        covered_months += 1
                        break

        return covered_months
