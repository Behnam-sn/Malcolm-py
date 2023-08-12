from openpyxl import Workbook, load_workbook

from config import Config
from domain.record import Record


class Excel_Utils:
    @staticmethod
    def create_new_excel() -> Workbook:
        excel = Workbook()
        return excel

    @staticmethod
    def create_new_sheet(excel: Workbook, name: str):
        sheet = excel.create_sheet(name)
        return sheet

    @staticmethod
    def save_excel(excel: Workbook, path: str = ".", name: str = "excel"):
        excel.save(f"{path}\\{name}.xlsx")

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
                date=row[Config.ITEM_DATE],
                day_in_week=row[Config.ITEM_DAY_IN_WEEK],
                start_time=row[Config.ITEM_START_TIME],
                category=row[Config.ITEM_CATEGORY],
                subject=row[Config.ITEM_SUBJECT],
                detail=row[Config.ITEM_DETAIL],
                time_spent=row[Config.ITEM_TIME_SPENT],
            )

            records.append(record)

        return records

    @staticmethod
    def fill_sheet_by_list_of_dictionary(sheet, items: list[dict]) -> None:
        for row_index, item in enumerate(items):
            for col_index, value in enumerate(item.values()):
                sheet.cell(row=row_index + 2, column=col_index + 1, value=value)  # type: ignore
