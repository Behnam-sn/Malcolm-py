from application.excel_utils import Excel_Utils
from application.utils import Utils
from config import Config
from domain.processor import Processor


class Application:
    @staticmethod
    def generate_entery_and_exit_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        items = Processor.generate_entery_and_exit_items(records)
        Utils.items_to_text_file(items, Config.ENTERY_AND_EXIT_REPORT_FILE_NAME)

    @staticmethod
    def generate_daily_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        items = Processor.generate_daily_items(records)
        Utils.items_to_text_file(items, Config.DAILY_REPORT_FILE_NAME)

    @staticmethod
    def generate_weekly_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        items = Processor.generate_weekly_items(records)
        Utils.items_to_text_file(items, Config.WEEKLY_REPORT_FILE_NAME)

    @staticmethod
    def generate_monthly_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        items = Processor.generate_monthly_items(records)
        Utils.items_to_text_file(items, Config.MONTHLY_REPORT_FILE_NAME)

    @staticmethod
    def generate_full_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)

        excel = Excel_Utils.create_new_excel()

        Utils.generate_entery_and_exit_report_sheet(excel, records)
        Utils.generate_daily_report_sheet(excel, records)
        Utils.generate_weekly_report_sheet(excel, records)
        Utils.generate_monthly_report_sheet(excel, records)

        Excel_Utils.save_excel(
            excel=excel,
            path=Config.OUTPUT_FOLDER_NAME,
            name=Config.OUTPUT_EXCEL_FILE_NAME,
        )
