from domain.time import Time


class Monthly:
    # id: int
    # category: str
    # subject: str | None
    # time: Time = field(default_factory=Time)

    def __init__(self, id: int, category: str, subject: str | None):
        self.id = id
        self.category = category
        self.subject = subject
        self.time = Time()
        self.category_total_time = Time()
        self.category_percentage: int = 0

    def set_category_total_time(self, category_total_time):
        self.category_total_time = category_total_time

    def set_category_percentage(self, category_percentage):
        self.category_percentage = category_percentage

    def convert_to_dictionary(self):
        return {
            "دسته بندی": self.category,
            "موضوع": self.subject,
            "مدت زمان صرف شده": self.time.convert_to_string(),
            "مجموع": self.category_total_time.convert_to_string(),
            "درصد": self.category_percentage,
        }
