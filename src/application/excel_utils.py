from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.worksheet import Worksheet

from config import Config
from domain.record import Record


class Excel_Utils:
    @staticmethod
    def create_workbook() -> Workbook:
        workbook = Workbook()
        return workbook

    @staticmethod
    def create_sheet(workbook: Workbook, name: str) -> Worksheet:
        sheet = workbook.create_sheet(name)
        return sheet

    @staticmethod
    def delete_default_sheet(workbook: Workbook):
        sheet_names = workbook.sheetnames
        default_sheet_name = sheet_names[0]
        default_sheet = workbook.get_sheet_by_name(default_sheet_name)
        Excel_Utils.delete_sheet(workbook, default_sheet)

    @staticmethod
    def delete_sheet(workbook: Workbook, sheet: Worksheet):
        workbook.remove_sheet(sheet)

    @staticmethod
    def change_sheet_direction_from_right_to_left(sheet: Worksheet):
        sheet.sheet_view.rightToLeft = True

    @staticmethod
    def automatically_adjust_width_of_workbook_columns(workbook: Workbook):
        for sheet_name in workbook.sheetnames:
            sheet = workbook.get_sheet_by_name(sheet_name)
            Excel_Utils.automatically_adjust_width_of_sheet_columns(sheet)

    @staticmethod
    def automatically_adjust_width_of_sheet_columns(sheet):
        padding = 3

        for column in sheet.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                try:  # Necessary to avoid error on empty cells
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass

            adjusted_width = max_length + padding
            sheet.column_dimensions[column_letter].width = adjusted_width

    @staticmethod
    def adjust_height_of_workbook_rows(workbook: Workbook, height: int):
        for sheet_name in workbook.sheetnames:
            sheet = workbook.get_sheet_by_name(sheet_name)
            Excel_Utils.adjust_height_of_sheet_rows(sheet, height)

    @staticmethod
    def adjust_height_of_sheet_rows(sheet, height: int):
        sheet_rows_length = sheet.max_row

        for row_id in range(1, sheet_rows_length + 1):
            sheet.row_dimensions[row_id].height = height

    @staticmethod
    def save_excel(excel: Workbook, path: str = ".", name: str = "excel"):
        try:
            excel.save(f"{path}\\{name}.xlsx")
        except PermissionError:
            print("Close Excel File Please")

    @staticmethod
    def extract_records_from_excel(excel_file_path: str) -> list[Record]:
        records = []
        record_last_id = 0

        workbook = load_workbook(
            data_only=True,
            filename=excel_file_path,
        )
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
    def add_headlines_to_sheet(sheet: Worksheet, items: list[str]) -> None:
        row_index = sheet.max_row

        for column_index, value in enumerate(items):
            column_index += 1
            cell = sheet.cell(row=row_index, column=column_index)

            cell.value = value
            cell.font = Font(
                name=Config.FONT_NAME,
                size=Config.HEADLINE_FONT_SIZE,
                bold=True,
            )
            cell.alignment = Alignment(
                horizontal="center",
                vertical="center",
            )

    @staticmethod
    def add_list_of_dictionary_to_sheet(sheet: Worksheet, items: list[dict]) -> None:
        row_index = sheet.max_row

        for item in items:
            row_index += 1

            for column_index, value in enumerate(item.values()):
                column_index += 1
                cell = sheet.cell(row=row_index, column=column_index)

                cell.value = value
                cell.font = Font(
                    name=Config.FONT_NAME,
                    size=Config.LINE_FONT_SIZE,
                )
                cell.alignment = Alignment(
                    horizontal="center",
                    vertical="center",
                )

    @staticmethod
    def add_dictionary_to_sheet(sheet: Worksheet, dictionary: dict) -> None:
        row_index = sheet.max_row
        row_index += 1

        for column_index, value in enumerate(dictionary.values()):
            column_index += 1
            cell = sheet.cell(row=row_index, column=column_index)

            cell.value = value
            cell.font = Font(
                name=Config.FONT_NAME,
                size=Config.LINE_FONT_SIZE,
            )
            cell.alignment = Alignment(
                horizontal="center",
                vertical="center",
            )
