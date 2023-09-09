from domain.monthly import Monthly
from domain.time import Time


class Category_Summary:
    def __init__(self):
        self.monthlies: list[Monthly] = []
        self.subjects: set[str] = set()
        self.total_time = Time()
        self.month_total_time = Time()
        self.category_percentage: float = 0

    def add_to_monthlies(self, monthly):
        self.monthlies.append(monthly)
        self.subjects.add(monthly.subject)

    def set_month_total_time(self, month_total_time):
        self.month_total_time = month_total_time

    def compute_total_time(self):
        for monthly in self.monthlies:
            self.total_time += monthly.time

    def set_monthlies_category_total_time(self):
        for monthly in self.monthlies:
            monthly.set_category_total_time(self.total_time)

    def compute_percentage(self):
        total_time_by_minute = self.total_time.convert_to_minutes()
        month_total_time_by_minute = self.month_total_time.convert_to_minutes()
        percentage = (total_time_by_minute * 100) / month_total_time_by_minute
        self.category_percentage = round(percentage, 1)

    def set_monthlies_category_percentage(self):
        for monthly in self.monthlies:
            monthly.set_category_percentage(self.category_percentage)
