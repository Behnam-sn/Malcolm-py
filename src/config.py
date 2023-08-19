class Config:
    INPUT_EXCEL_FILE_PATH = "C:\\Users\\Behnam\\Downloads\\dorcci.xlsx"

    OUTPUT_FOLDER_NAME = "dist"
    OUTPUT_EXCEL_FILE_NAME = "Report"
    ENTERY_AND_EXIT_REPORT_FILE_NAME = "entery and exit report"
    DAILY_REPORT_FILE_NAME = "daily report"
    WEEKLY_REPORT_FILE_NAME = "weekly report"
    MONTHLY_REPORT_FILE_NAME = "monthly report"

    ENTERY_AND_EXIT_SHEET_NAME = "ورود و خروج"
    DAILY_REPORT_SHEET_NAME = "گزارش روزانه"
    WEEKLY_REPORT_SHEET_NAME = "گزارش هفتگی"
    MONTHLY_REPORT_SHEET_NAME = "گزارش ماهانه"

    DATE_INDEX = 0
    DAY_IN_WEEK_INDEX = 1
    START_TIME_INDEX = 2
    CATEGORY_INDEX = 3
    SUBJECT_INDEX = 4
    DETAIL_INDEX = 5
    TIME_SPENT_INDEX = 6

    WEEKS = [
        [3, 9],
        [10, 16],
        [17, 23],
        [24, 30],
    ]

    CATEGORIES = [
        "دانش نامه",
        "جلسه",
        "مطالعه",
        "گزارش",
        "صورت جلسه",
        "متفرقه",
    ]

    FONT_NAME = "Shabnam FD"
    HEADLINE_FONT_SIZE = 11
    LINE_FONT_SIZE = 10

    ROW_HEIGHT = 28
