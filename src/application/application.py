from application.excel_utils import Excel_Utils
from application.file_utils import File_Utils
from application.utils import Utils
from config import Config
from domain.processor import Processor


class Application:
    @staticmethod
    def generate_entery_and_exit_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        items = Processor.generate_entery_and_exit_items(records)
        dictionaries = Utils.convert_list_of_items_to_list_of_dictionaries(items)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=dictionaries,
            file_name=Config.ENTERY_AND_EXIT_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_daily_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        dailies = Processor.generate_daily_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(dailies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.DAILY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_weekly_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        weeklies = Processor.generate_weekly_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(weeklies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.WEEKLY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_monthly_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)
        monthlies = Processor.generate_monthly_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(monthlies)
        File_Utils.generate_text_file_from_list_of_dictionaries(
            items=items,
            file_name=Config.MONTHLY_REPORT_FILE_NAME,
            separator="\t",
        )

    @staticmethod
    def generate_full_report() -> None:
        records = Excel_Utils.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)

        excel = Excel_Utils.create_workbook()

        Utils.generate_entery_and_exit_report_sheet(excel, records)
        Utils.generate_daily_report_sheet(excel, records)
        Utils.generate_weekly_report_sheet(excel, records)
        Utils.generate_monthly_report_sheet(excel, records)

        Excel_Utils.automatically_adjust_width_of_workbook_columns(excel)
        Excel_Utils.adjust_height_of_workbook_rows(excel, Config.ROW_HEIGHT)

        Excel_Utils.delete_default_sheet(excel)
        Excel_Utils.save_excel(
            excel=excel,
            path=Config.OUTPUT_FOLDER_NAME,
            name=Config.OUTPUT_EXCEL_FILE_NAME,
        )
