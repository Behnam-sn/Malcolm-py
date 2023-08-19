from config import Config
from domain.entery_and_exit import Entery_And_Exit
from domain.entery_and_exit_summary import Entery_And_Exit_Summary
from domain.record import Record
from domain.time import Time
from domain.utils import Utils


class Processor:
    @staticmethod
    def generate_entery_and_exit_items(records: list[Record]) -> list[Entery_And_Exit]:
        filtered_records = Utils.filter_records_by_category(
            records=records, include=["ورود", "خروج"]
        )
        entery_and_exits = Utils.excract_entery_and_exits_from_records(filtered_records)
        return entery_and_exits
        # return Utils.convert_item_to_dictionary(items)

    @staticmethod
    def generate_entery_and_exit_sammary(
        entery_and_exits: list[Entery_And_Exit],
    ) -> Entery_And_Exit_Summary:
        total_days: int = 0
        total_entery_time = Time()
        total_exit_time = Time()
        total_time = Time()

        for entery_and_exit in entery_and_exits:
            total_days += 1
            total_entery_time += entery_and_exit.entery_time
            total_exit_time += entery_and_exit.exit_time
            total_time += entery_and_exit.total_time

        average_entery_time_by_minutes = int(
            total_entery_time.convert_to_minutes() / total_days
        )
        average_entery_time = Time.convert_minutes_to_time(
            average_entery_time_by_minutes
        )

        average_exit_time_by_minutes = int(
            total_exit_time.convert_to_minutes() / total_days
        )
        average_exit_time = Time.convert_minutes_to_time(average_exit_time_by_minutes)

        summary = Entery_And_Exit_Summary(
            total_days,
            average_entery_time,
            average_exit_time,
            total_time,
        )
        return summary

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

    @staticmethod
    def sort_items(items: list[dict]) -> list[dict]:
        sorted_summary = {
            "دانش نامه": [],
            "جلسه": [],
            "مطالعه": [],
            "توسعه": [],
            "گزارش": [],
            "صورت جلسه": [],
            "متفرقه": [],
        }

        for item in items:
            if item["دسته بندی"] not in sorted_summary:
                sorted_summary[item["دسته بندی"]] = []

            sorted_summary[item["دسته بندی"]].append(item)

        list = []

        for item in sorted_summary.values():
            for to in item:
                list.append(to)

        return list
