from dataclasses import dataclass
import datetime


@dataclass
class Record:
    id: int
    date: str
    day_in_week: str
    start_time: datetime.time
    category: str
    subject: str | None
    detail: str | None
    time_spent: datetime.time | None

    def get_day(self):
        return self.date[len(self.date) - 2 :]
