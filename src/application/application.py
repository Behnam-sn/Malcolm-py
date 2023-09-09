from application.excel_utils import Excel_Utils
from application.file_utils import File_Utils
from application.utils import Utils
from config import Config
from domain.processor import Processor
from domain.record import Record


class Application:
    @staticmethod
    def extract_records_from_excel(excel_file_path: str) -> list[Record]:
        records = []
        record_last_id = 0

        workbook = Excel_Utils.load_workbook(excel_file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):  # type: ignore
            record_last_id += 1

            record = Record(
                id=record_last_id,
                date=row[Config.DATE_INDEX],
                day_in_week=row[Config.DAY_IN_WEEK_INDEX],
                start_time=row[Config.START_TIME_INDEX],
                category=row[Config.CATEGORY_INDEX],
                subject=row[Config.SUBJECT_INDEX],
                detail=row[Config.DETAIL_INDEX],
                time_spent=row[Config.TIME_SPENT_INDEX],
            )

            records.append(record)

        return records

    @staticmethod
    def generate_enter_and_exit_report(records: list[Record]) -> None:
        items = Processor.generate_enter_and_exit_items(records)
        dictionaries = Utils.convert_list_of_items_to_list_of_dictionaries(items)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=dictionaries,
            file_name=Config.ENTER_AND_EXIT_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_daily_report(records: list[Record]) -> None:
        dailies = Processor.generate_daily_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(dailies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.DAILY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_weekly_report(records: list[Record]) -> None:
        weeklies = Processor.generate_weekly_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(weeklies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.WEEKLY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_monthly_report(records: list[Record]) -> None:
        monthlies = Processor.generate_monthly_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(monthlies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.MONTHLY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_full_report(records: list[Record]) -> None:
        workbook = Excel_Utils.create_workbook()

        Utils.generate_enter_and_exit_report_sheet(workbook, records)
        Utils.generate_daily_report_sheet(workbook, records)
        Utils.generate_weekly_report_sheet(workbook, records)
        Utils.generate_monthly_report_sheet(workbook, records)

        Excel_Utils.automatically_adjust_width_of_workbook_columns(workbook)
        Excel_Utils.adjust_height_of_workbook_rows(workbook, Config.ROW_HEIGHT)

        Excel_Utils.delete_default_sheet(workbook)
        Excel_Utils.save_workbook(
            workbook=workbook,
            path=Config.OUTPUT_FOLDER_NAME,
            name=Config.OUTPUT_EXCEL_FILE_NAME,
        )
