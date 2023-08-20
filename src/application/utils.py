from openpyxl import Workbook
from openpyxl.cell import Cell
from openpyxl.styles import PatternFill
from openpyxl.styles.colors import Color
from openpyxl.worksheet.worksheet import Worksheet

from application.excel_utils import Excel_Utils
from config import Config
from domain.processor import Processor
from domain.record import Record


class Utils:
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
        sheet = Excel_Utils.create_sheet_with_default_options(
            workbook=workbook,
            name=Config.ENTERY_AND_EXIT_SHEET_NAME,
        )

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
        sheet = Excel_Utils.create_sheet_with_default_options(
            workbook=workbook,
            name=Config.DAILY_REPORT_SHEET_NAME,
        )

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

        Utils.format_catoegories(sheet=sheet, catoegories_column_index=4)
        Utils.merge_identical_cells_by_column(sheet=sheet, column_index=1)
        Utils.merge_identical_cells_by_column(sheet=sheet, column_index=2)

    @staticmethod
    def generate_weekly_report_sheet(workbook: Workbook, records: list[Record]) -> None:
        sheet = Excel_Utils.create_sheet_with_default_options(
            workbook=workbook,
            name=Config.WEEKLY_REPORT_SHEET_NAME,
        )

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

        Utils.format_catoegories(sheet=sheet, catoegories_column_index=2)
        Utils.merge_identical_cells_by_column(sheet=sheet, column_index=1)
        Utils.merge_identical_cells_by_column(sheet=sheet, column_index=2)

    @staticmethod
    def generate_monthly_report_sheet(
        workbook: Workbook, records: list[Record]
    ) -> None:
        sheet = Excel_Utils.create_sheet_with_default_options(
            workbook=workbook,
            name=Config.MONTHLY_REPORT_SHEET_NAME,
        )

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

        Utils.format_catoegories(sheet=sheet, catoegories_column_index=1)
        Utils.merge_identical_cells_by_column(sheet=sheet, column_index=1)

    @staticmethod
    def format_catoegories(sheet: Worksheet, catoegories_column_index: int) -> None:
        for row in sheet.iter_rows(
            min_col=catoegories_column_index, max_col=catoegories_column_index
        ):
            for cell in row:
                catoegory = cell.value
                if catoegory in Config.CATEGORIES_COLOR:
                    rgb_color = Config.CATEGORIES_COLOR[catoegory]
                    color = Color(rgb=rgb_color)
                    cell.fill = PatternFill(patternType="solid", fgColor=color)

    @staticmethod
    def merge_identical_cells_by_column(sheet: Worksheet, column_index: int) -> None:
        last_row_index = Excel_Utils.compute_last_row_index(sheet)

        target_cell = None

        for row_index in range(1, last_row_index + 1):
            current_cell = Excel_Utils.select_cell(sheet, row_index, column_index)

            if row_index == 1:
                target_cell = current_cell
                continue

            if current_cell.value == target_cell.value and row_index != last_row_index:  # type: ignore
                continue

            cells_gape = current_cell.row - target_cell.row  # type: ignore
            if cells_gape == 1:
                target_cell = current_cell
                continue

            if row_index == last_row_index:
                Excel_Utils.merge_cells(sheet, target_cell, current_cell)  # type: ignore
                continue

            previous_cell = Excel_Utils.select_cell(sheet, row_index - 1, column_index)
            Excel_Utils.merge_cells(sheet, target_cell, previous_cell)  # type: ignore
            target_cell = current_cell
