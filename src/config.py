class Config:
    INPUT_EXCEL_FILE_PATH = (
        "C:\\Users\\Behnam\\OneDrive\\Tiba\\Reports\\1402-05 اطلاعات مرداد.xlsx"
    )

    OUTPUT_FOLDER_NAME = "dist"
    OUTPUT_EXCEL_FILE_NAME = "Report"
    ENTER_AND_EXIT_REPORT_FILE_NAME = "enter and exit report"
    DAILY_REPORT_FILE_NAME = "daily report"
    WEEKLY_REPORT_FILE_NAME = "weekly report"
    MONTHLY_REPORT_FILE_NAME = "monthly report"

    ENTER_AND_EXIT_SHEET_NAME = "ورود و خروج"
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

    CATEGORIES_COLOR = {
        "دانش نامه": "A9D08E",
        "توسعه": "FF4D4D",
        "جلسه": "FFD966",
        "مطالعه": "F4B084",
        "گزارش": "8EA9DB",
        "صورت جلسه": "C9C9C9",
    }

    SUMMARY_COLOR = "92D050"

    FONT_NAME = "Shabnam FD"
    HEADLINE_FONT_SIZE = 11
    LINE_FONT_SIZE = 10

    ROW_HEIGHT = 28
