from config import Config
from domain.daily import Daily
from domain.date_utils import Date_Utils
from domain.entery_and_exit import Entery_And_Exit
from domain.monthly import Monthly
from domain.record import Record
from domain.weekly import Weekly


class Utils:
    @staticmethod
    def filter_records_by_category(
        records: list[Record],
        include: list[str] | None = None,
        exclude: list[str] | None = None,
    ) -> list[Record]:
        filtered_records = []

        for record in records:
            if exclude != None and record.category in exclude:
                continue

            if include == None:
                filtered_records.append(record)

            elif record.category in include:
                filtered_records.append(record)

        return filtered_records

    @staticmethod
    def filter_records_by_date(records: list[Record], start, end) -> list[Record]:
        start = Date_Utils.number_to_string(start)
        end = Date_Utils.number_to_string(end)

        filtered_records = filter(
            lambda record: (start <= record.get_day() and end >= record.get_day()),
            records,
        )

        return list(filtered_records)

    @staticmethod
    def convert_record_to_daily(records: list[Record]) -> list[Daily]:
        dailies = []
        daily_last_id = 0

        for record in records:
            daily_last_id += 1

            daily = Daily(
                id=daily_last_id,
                date=record.date,
                day_in_week=record.day_in_week,
                start_time=record.start_time,
                category=record.category,
                subject=record.subject,
                detail=record.detail,
                time_spent=record.time_spent,
            )

            dailies.append(daily)

        return dailies

    @staticmethod
    def convert_item_to_dictionary(items: list) -> list[dict]:
        list = []

        for item in items:
            list.append(item.convert_to_dictionary())

        return list

    @staticmethod
    def excract_entery_and_exits_from_records(records: list[Record]):
        logs: dict[str, Entery_And_Exit] = {}
        log_last_id = 0

        for record in records:
            if record.date not in logs:
                log_last_id += 1
                logs[record.date] = Entery_And_Exit(id=log_last_id, date=record.date)

            if record.category == "ورود":
                logs[record.date].set_entery_time(record.start_time)

            if record.category == "خروج":
                logs[record.date].set_exit_time(record.start_time)

        return list(logs.values())

    @staticmethod
    def excract_weeklies_from_records(records: list[Record]) -> list[Weekly]:
        weeklies: list[Weekly] = []
        week_last_id = 0
        weekly_last_id = 0

        for week in Config.WEEKS:
            week_last_id += 1

            filtered_records = Utils.filter_records_by_date(
                records=records, start=week[0], end=week[1]
            )

            for record in filtered_records:
                weekly = Utils.find_weekly_in_list(
                    weeklies=weeklies,
                    week_id=week_last_id,
                    category=record.category,
                    subject=record.subject,
                )

                if weekly == None:
                    weekly_last_id += 1
                    weekly = Weekly(
                        id=weekly_last_id,
                        week_id=week_last_id,
                        category=record.category,
                        subject=record.subject,
                    )
                    weeklies.append(weekly)

                weekly.time.increase_hour(amount=record.time_spent.hour)  # type: ignore
                weekly.time.increace_minute(amount=record.time_spent.minute)  # type: ignore

        sorted_summary = {
            "دانش نامه": [],
            "جلسه": [],
            "مطالعه": [],
            "توسعه": [],
            "گزارش": [],
            "صورت جلسه": [],
            "متفرقه": [],
        }

        ddd = {}

        for we in weeklies:
            if we.week_id not in ddd:
                ddd[we.week_id] = {
                    "دانش نامه": [],
                    "جلسه": [],
                    "مطالعه": [],
                    "توسعه": [],
                    "گزارش": [],
                    "صورت جلسه": [],
                    "متفرقه": [],
                }

            ddd[we.week_id][we.category].append(we)

        listt = []
        for kk in ddd.values():
            for aa in kk.values():
                for ak in aa:
                    listt.append(ak)

        return listt

    @staticmethod
    def excract_monthlies_from_records(records: list[Record]) -> list[Monthly]:
        monthlies = []
        monthly_last_id = 0

        for record in records:
            monthly = Utils.find_monthly_in_list(
                monthlies=monthlies,
                category=record.category,
                subject=record.subject,
            )

            if monthly == None:
                monthly_last_id += 1
                monthly = Monthly(
                    id=monthly_last_id,
                    category=record.category,
                    subject=record.subject,
                )
                monthlies.append(monthly)

            monthly.time.increase_hour(amount=record.time_spent.hour)  # type: ignore
            monthly.time.increace_minute(amount=record.time_spent.minute)  # type: ignore

        return monthlies

    @staticmethod
    def find_weekly_in_list(
        weeklies: list[Weekly],
        week_id: int,
        category: str,
        subject: str | None,
    ) -> Weekly | None:
        for weekly in weeklies:
            if (
                weekly.week_id == week_id
                and weekly.category == category
                and weekly.subject == subject
            ):
                return weekly

        return None

    @staticmethod
    def find_monthly_in_list(
        monthlies: list[Monthly],
        category: str,
        subject: str | None,
    ) -> Monthly | None:
        for monthly in monthlies:
            if monthly.category == category and monthly.subject == subject:
                return monthly

        return None
