from application.application import Application
from config import Config

if __name__ == "__main__":
    records = Application.extract_records_from_excel(Config.INPUT_EXCEL_FILE_PATH)

    Application.generate_enter_and_exit_report(records)
    Application.generate_daily_report(records)
    Application.generate_weekly_report(records)
    Application.generate_monthly_report(records)
    Application.generate_full_report(records)

    # todo: weekly summary
    # todo: monthly summary
    # todo: config cell padding
    # todo: write a better category sort method
    # todo: write a better merge method
