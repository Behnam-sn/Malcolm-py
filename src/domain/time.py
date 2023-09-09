from dataclasses import dataclass

from domain.date_utils import Date_Utils


@dataclass
class Time:
    hour: int = 0
    minute: int = 0

    def increase_hour(self, amount: int) -> None:
        self.hour += amount

    def increase_minute(self, amount: int) -> None:
        self.minute += amount

        if self.minute >= 60:
            hour = int(self.minute / 60)
            self.hour += hour
            self.minute = self.minute % 60

    def convert_to_minutes(self) -> int:
        return (self.hour * 60) + self.minute

    def convert_to_string(self) -> str:
        return f"{Date_Utils.number_to_string(self.hour)}:{Date_Utils.number_to_string(self.minute)}"

    def __add__(self, time):
        new_time = Time(self.hour, self.minute)
        new_time.increase_hour(time.hour)
        new_time.increase_minute(time.minute)
        return new_time

    @staticmethod
    def convert_minutes_to_time(minutes: int):
        hour: int = int(minutes / 60)
        minute: int = minutes % 60

        return Time(
            hour,
            minute,
        )
