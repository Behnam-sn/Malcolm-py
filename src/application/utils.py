from openpyxl import Workbook

from application.excel_utils import Excel_Utils
from config import Config
from domain.processor import Processor
from domain.record import Record


class Utils:
    @staticmethod
    def generate_entery_and_exit_report_sheet(
        workbook: Workbook,
        records: list[Record],
    ) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.ENTERY_AND_EXIT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)

        items = Processor.generate_entery_and_exit_items(records)
        headlines = Utils.extract_headline_from_item(items)

        Excel_Utils.add_headlines_to_sheet(sheet, headlines)
        Excel_Utils.add_list_of_dictionary_to_sheet(sheet, items)

    @staticmethod
    def generate_daily_report_sheet(workbook: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.DAILY_REPORT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)
        items = Processor.generate_daily_items(records)
        headlines = Utils.extract_headline_from_item(items)

        Excel_Utils.add_headlines_to_sheet(sheet, headlines)
        Excel_Utils.add_list_of_dictionary_to_sheet(sheet, items)

    @staticmethod
    def generate_weekly_report_sheet(workbook: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.WEEKLY_REPORT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)
        items = Processor.generate_weekly_items(records)
        headlines = Utils.extract_headline_from_item(items)

        Excel_Utils.add_headlines_to_sheet(sheet, headlines)
        Excel_Utils.add_list_of_dictionary_to_sheet(sheet, items)

    @staticmethod
    def generate_monthly_report_sheet(
        workbook: Workbook, records: list[Record]
    ) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.MONTHLY_REPORT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)
        items = Processor.generate_monthly_items(records)
        sorted_items = Processor.sort_items(items=items)
        headlines = Utils.extract_headline_from_item(items)

        Excel_Utils.add_headlines_to_sheet(sheet, headlines)
        Excel_Utils.add_list_of_dictionary_to_sheet(sheet, sorted_items)

    @staticmethod
    def extract_headline_from_item(items: list) -> list[str]:
        headlines = []
        item = items[0]
        for key in item:
            headlines.append(key)
        return headlines
