from domain.daily import Daily
from domain.enter_and_exit import Enter_And_Exit
from domain.enter_and_exit_summary import Enter_And_Exit_Summary
from domain.monthly import Monthly
from domain.monthly_summary import Monthly_Summary
from domain.record import Record
from domain.time import Time
from domain.utils import Utils
from domain.weekly import Weekly


class Processor:
    @staticmethod
    def generate_enter_and_exit_items(records: list[Record]) -> list[Enter_And_Exit]:
        filtered_records = Utils.filter_records_by_category(
            records=records, include=["ورود", "خروج"]
        )
        return Utils.extract_enter_and_exits_from_records(filtered_records)

    @staticmethod
    def generate_daily_items(records: list[Record]) -> list[Daily]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        return Utils.convert_record_to_daily(filtered_records)

    @staticmethod
    def generate_weekly_items(records: list[Record]) -> list[Weekly]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        return Utils.extract_weeklies_from_records(filtered_records)

    @staticmethod
    def generate_monthly_items(records: list[Record]) -> list[Monthly]:
        filtered_records = Utils.filter_records_by_category(
            records=records, exclude=["ورود", "خروج"]
        )
        return Utils.extract_monthlies_from_records(filtered_records)

    @staticmethod
    def generate_enter_and_exit_summary(
        enter_and_exits: list[Enter_And_Exit],
    ) -> Enter_And_Exit_Summary:
        total_days: int = 0
        total_enter_time = Time()
        total_exit_time = Time()
        total_time = Time()

        for enter_and_exit in enter_and_exits:
            total_days += 1
            total_enter_time += enter_and_exit.enter_time
            total_exit_time += enter_and_exit.exit_time
            total_time += enter_and_exit.total_time

        average_enter_time_by_minutes = int(
            total_enter_time.convert_to_minutes() / total_days
        )
        average_enter_time = Time.convert_minutes_to_time(average_enter_time_by_minutes)

        average_exit_time_by_minutes = int(
            total_exit_time.convert_to_minutes() / total_days
        )
        average_exit_time = Time.convert_minutes_to_time(average_exit_time_by_minutes)

        return Enter_And_Exit_Summary(
            total_days,
            average_enter_time,
            average_exit_time,
            total_time,
        )

    @staticmethod
    def generate_monthly_summary(monthly_items: list[Monthly]) -> Monthly_Summary:
        monthly_summary = Monthly_Summary(monthly_items)

        monthly_summary.compute_category_summaries_total_time()
        monthly_summary.compute_total_time()
        monthly_summary.set_category_summaries_month_total_time()

        return monthly_summary

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
