from openpyxl import Workbook

from application.excel_utils import Excel_Utils
from config import Config
from domain.processor import Processor
from domain.record import Record


class Utils:
    @staticmethod
    def generate_entery_and_exit_report_sheet(
        excel: Workbook, records: list[Record]
    ) -> None:
        sheet = Excel_Utils.create_new_sheet(
            excel=excel, name=Config.ENTERY_AND_EXIT_SHEET_NAME
        )
        items = Processor.generate_entery_and_exit_items(records)
        Excel_Utils.fill_sheet_by_list_of_dictionary(sheet, items)

    @staticmethod
    def generate_daily_report_sheet(excel: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_new_sheet(
            excel=excel, name=Config.DAILY_REPORT_SHEET_NAME
        )
        items = Processor.generate_daily_items(records)
        Excel_Utils.fill_sheet_by_list_of_dictionary(sheet, items)

    @staticmethod
    def generate_weekly_report_sheet(excel: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_new_sheet(
            excel=excel, name=Config.WEEKLY_REPORT_SHEET_NAME
        )
        items = Processor.generate_weekly_items(records)
        Excel_Utils.fill_sheet_by_list_of_dictionary(sheet, items)

    @staticmethod
    def generate_monthly_report_sheet(excel: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_new_sheet(
            excel=excel, name=Config.MONTHLY_REPORT_SHEET_NAME
        )
        items = Processor.generate_monthly_items(records)
        Excel_Utils.fill_sheet_by_list_of_dictionary(sheet, items)
