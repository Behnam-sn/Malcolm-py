import datetime
from dataclasses import dataclass, field

from domain.time import Time


@dataclass
class Entery_And_Exit:
    id: int
    date: str
    entery_time: Time | None = None
    exit_time: Time | None = None
    total_time: Time = field(default_factory=Time)

    def convert_to_dictionary(self):
        return {
            "تاریخ": self.date,
            "ساعت ورود": self.entery_time.convert_to_string()
            if self.entery_time != None
            else None,
            "ساعت خروج": self.exit_time.convert_to_string()
            if self.exit_time != None
            else None,
            "مجموع ساعت": self.total_time.convert_to_string(),
        }

    def set_entery_time(self, time: datetime.time):
        self.entery_time = Time(hour=time.hour, minute=time.minute)
        self.compute_total_time()

    def set_exit_time(self, time: datetime.time):
        self.exit_time = Time(hour=time.hour, minute=time.minute)
        self.compute_total_time()

    def compute_total_time(self):
        if self.entery_time == None or self.exit_time == None:
            return

        hour = self.exit_time.hour - self.entery_time.hour

        if self.entery_time.minute > self.exit_time.minute:
            hour -= 1
            self.exit_time.minute += 60

        minute = self.exit_time.minute - self.entery_time.minute

        self.total_time.hour = hour
        self.total_time.minute = minute


def time_to_string(time: datetime.time | None) -> str | None:
    if time == None:
        return None

    return time.strftime("%H:%M")
