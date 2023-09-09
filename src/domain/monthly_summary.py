from domain.category_summary import Category_Summary
from domain.monthly import Monthly
from domain.time import Time


class Monthly_Summary:
    def __init__(self, monthly_items: list[Monthly]):
        self.category_summaries: dict[str, Category_Summary] = {}
        self.total_time = Time()

        for monthly in monthly_items:
            category = monthly.category

            if category not in self.category_summaries:
                self.category_summaries[category] = Category_Summary()

            self.category_summaries[category].add_to_monthlies(monthly)

    def compute_category_summaries_total_time(self):
        for category_summary in self.category_summaries.values():
            category_summary.compute_total_time()
            category_summary.set_monthlies_category_total_time()

    def compute_total_time(self):
        for category_summary in self.category_summaries.values():
            self.total_time += category_summary.total_time

    def set_category_summaries_month_total_time(self):
        for category_summary in self.category_summaries.values():
            category_summary.set_month_total_time(self.total_time)
            category_summary.compute_percentage()
            category_summary.set_monthlies_category_percentage()

    def compute_categories_subject_count(self) -> int:
        count = 0

        for category_summary in self.category_summaries.values():
            count += len(category_summary.subjects)

        return count

    def compute_categories_total_time(self) -> Time:
        total_time = Time()

        for category_summary in self.category_summaries.values():
            total_time += category_summary.total_time

        return total_time

    def compute_categories_total_percentage(self) -> float:
        total_percentage = 0

        for category_summary in self.category_summaries.values():
            total_percentage += category_summary.category_percentage

        return total_percentage

    def convert_to_list_of_dictionaries(self) -> list[dict[str, str]]:
        list = []

        for category_summary in self.category_summaries.values():
            for monthly in category_summary.monthlies:
                list.append(monthly.convert_to_dictionary())

        return list

    def convert_to_dictionary(self) -> dict:
        return {
            "مجموع تعداد دسته بندی ها": len(self.category_summaries),
            "مجموع تعداد موضوع ها": self.compute_categories_subject_count(),
            "مجموع مدت زمان صرف شده": self.compute_categories_total_time().convert_to_string(),
            "مجموع مجموع": self.total_time.convert_to_string(),
            "مجموع درصد": self.compute_categories_total_percentage(),
        }
