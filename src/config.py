class Config:
    INPUT_EXCEL_FILE_PATH = "C:\\Users\\Behnam\\Downloads\\lfeo.xlsx"

    OUTPUT_FOLDER_NAME = "dist"
    OUTPUT_EXCEL_FILE_NAME = "Report"
    ENTERY_AND_EXIT_REPORT_FILE_NAME = "time report"
    DAILY_REPORT_FILE_NAME = "daily report"
    WEEKLY_REPORT_FILE_NAME = "weekly report"
    MONTHLY_REPORT_FILE_NAME = "monthly report"

    ENTERY_AND_EXIT_SHEET_NAME = "ورود و خروج"
    DAILY_REPORT_SHEET_NAME = "گزارش روزانه"
    WEEKLY_REPORT_SHEET_NAME = "گزارش هفتگی"
    MONTHLY_REPORT_SHEET_NAME = "گزارش ماهانه"

    ITEM_DATE = 0
    ITEM_DAY_IN_WEEK = 1
    ITEM_START_TIME = 2
    ITEM_CATEGORY = 3
    ITEM_SUBJECT = 4
    ITEM_DETAIL = 5
    ITEM_TIME_SPENT = 6

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
