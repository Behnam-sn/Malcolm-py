from openpyxl import Workbook

from application.excel_utils import Excel_Utils
from config import Config
from domain.processor import Processor
from domain.record import Record


class Utils:
    @staticmethod
    def convert_list_of_items_to_list_of_dictionaries(
        items: list,
    ) -> list[dict[str, str]]:
        list = []

        for item in items:
            list.append(item.convert_to_dictionary())

        return list

    @staticmethod
    def extract_headline_from_item(item: dict) -> list[str]:
        headlines = []

        for key in item:
            headlines.append(key)

        return headlines

    @staticmethod
    def extract_headline_from_items(items: list) -> list[str]:
        headlines = []
        item = items[0]

        for key in item:
            headlines.append(key)

        return headlines

    @staticmethod
    def generate_entery_and_exit_report_sheet(
        workbook: Workbook, records: list[Record]
    ) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.ENTERY_AND_EXIT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)

        entery_and_exit = Processor.generate_entery_and_exit_items(records)
        items = Utils.convert_list_of_items_to_list_of_dictionaries(entery_and_exit)
        headlines = Utils.extract_headline_from_items(items)
        summary = Processor.generate_entery_and_exit_sammary(
            entery_and_exit
        ).convert_to_dictionary()
        summary_headlines = Utils.extract_headline_from_item(summary)

        Excel_Utils.appned_list_of_string_to_sheet(
            sheet=sheet,
            items=headlines,
            format_cell_method=Excel_Utils.format_cell_headline,
        )
        Excel_Utils.append_list_of_dictionary_to_sheet(
            sheet=sheet,
            items=items,
            format_cell_method=Excel_Utils.format_cell_default,
        )
        Excel_Utils.appned_list_of_string_to_sheet(
            sheet=sheet,
            items=summary_headlines,
            format_cell_method=Excel_Utils.format_cell_headline,
        )
        Excel_Utils.append_dictionary_to_sheet(
            sheet=sheet,
            dictionary=summary,
            format_cell_method=Excel_Utils.format_cell_default,
        )

    @staticmethod
    def generate_daily_report_sheet(workbook: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.DAILY_REPORT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)

        items = Processor.generate_daily_items(records)
        dicts = Utils.convert_list_of_items_to_list_of_dictionaries(items)
        headlines = Utils.extract_headline_from_items(dicts)

        Excel_Utils.appned_list_of_string_to_sheet(
            sheet=sheet,
            items=headlines,
            format_cell_method=Excel_Utils.format_cell_headline,
        )
        Excel_Utils.append_list_of_dictionary_to_sheet(
            sheet=sheet,
            items=dicts,
            format_cell_method=Excel_Utils.format_cell_default,
        )

    @staticmethod
    def generate_weekly_report_sheet(workbook: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_sheet(
            workbook=workbook,
            name=Config.WEEKLY_REPORT_SHEET_NAME,
        )
        Excel_Utils.change_sheet_direction_from_right_to_left(sheet)

        items = Processor.generate_weekly_items(records)
        dicts = Utils.convert_list_of_items_to_list_of_dictionaries(items)
        headlines = Utils.extract_headline_from_items(dicts)

        Excel_Utils.appned_list_of_string_to_sheet(
            sheet=sheet,
            items=headlines,
            format_cell_method=Excel_Utils.format_cell_headline,
        )
        Excel_Utils.append_list_of_dictionary_to_sheet(
            sheet=sheet,
            items=dicts,
            format_cell_method=Excel_Utils.format_cell_default,
        )

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
        dicts = Utils.convert_list_of_items_to_list_of_dictionaries(items)
        sorted_items = Processor.sort_items(items=dicts)
        headlines = Utils.extract_headline_from_items(dicts)

        Excel_Utils.appned_list_of_string_to_sheet(
            sheet=sheet,
            items=headlines,
            format_cell_method=Excel_Utils.format_cell_headline,
        )
        Excel_Utils.append_list_of_dictionary_to_sheet(
            sheet=sheet,
            items=sorted_items,
            format_cell_method=Excel_Utils.format_cell_default,
        )
