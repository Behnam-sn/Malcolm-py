from dataclasses import dataclass, field

from domain.time import Time


@dataclass
class Monthly:
    id: int
    category: str
    subject: str | None
    time: Time = field(default_factory=Time)

    def convert_to_dictionary(self):
        return {
            "دسته بندی": self.category,
            "موضوع": self.subject,
            "مدت زمان صرف شده": self.time.convert_to_string(),
        }
