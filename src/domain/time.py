from dataclasses import dataclass

from domain.date_utils import Date_Utils


@dataclass
class Time:
    hour: int = 0
    minute: int = 0

    def increase_hour(self, amount: int) -> None:
        self.hour += amount

    def increace_minute(self, amount: int) -> None:
        self.minute += amount

        if self.minute >= 60:
            hour = int(self.minute / 60)
            self.hour += hour
            self.minute = self.minute % 60

    def convert_to_string(self) -> str:
        return f"{Date_Utils.number_to_string(self.hour)}:{Date_Utils.number_to_string(self.minute)}"
