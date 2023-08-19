from application.application import Application

if __name__ == "__main__":
    Application.generate_entery_and_exit_report()
    Application.generate_daily_report()
    Application.generate_weekly_report()
    Application.generate_monthly_report()
    Application.generate_full_report()

    # todo: conditional rendering: daily, weekly, monthy
    # todo: sort catoegories
    # todo: calculate entery and exit
    # todo: weekly summary
    # todo: monthly summary
    # todo: merge
