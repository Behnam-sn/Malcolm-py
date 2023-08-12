from domain.record import Record
from domain.utils import Utils


class Processor:
    @staticmethod
    def generate_entery_and_exit_items(records: list[Record]) -> list[dict]:
        filtered_records = Utils.filter_records_by_category(
            records=records, include=["ورود", "خروج"]
        )
        items = Utils.excract_entery_and_exits_from_records(filtered_records)
        return Utils.convert_item_to_dictionary(items)

    @staticmethod
    def generate_daily_items(records: list[Record]) -> list[dict]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        items = Utils.convert_record_to_daily(filtered_records)
        return Utils.convert_item_to_dictionary(items)

    @staticmethod
    def generate_weekly_items(records: list[Record]) -> list[dict]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        items = Utils.excract_weeklies_from_records(filtered_records)
        return Utils.convert_item_to_dictionary(items)

    @staticmethod
    def generate_monthly_items(records: list[Record]) -> list[dict]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        items = Utils.excract_monthlies_from_records(filtered_records)
        return Utils.convert_item_to_dictionary(items)
