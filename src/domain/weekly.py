from dataclasses import dataclass, field

from domain.time import Time


@dataclass
class Weekly:
    id: int
    week_id: int
    category: str
    subject: str | None
    time: Time = field(default_factory=Time)

    def convert_to_dictionary(self):
        return {
            "شماره هفته": self.week_id,
            "دسته بندی": self.category,
            "موضوع": self.subject,
            "مدت زمان صرف شده": self.time.convert_to_string(),
        }
