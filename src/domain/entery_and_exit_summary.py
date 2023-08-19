from dataclasses import dataclass, field

from domain.time import Time


@dataclass
class Entery_And_Exit_Summary:
    total_days: int
    average_entery_time: Time = field(default_factory=Time)
    average_exit_time: Time = field(default_factory=Time)
    total_time: Time = field(default_factory=Time)

    def convert_to_dictionary(self):
        return {
            "مجموع روزها": self.total_days,
            "میانگین ساعت ورود": self.average_entery_time.convert_to_string(),
            "میانگین ساعت خروج": self.average_exit_time.convert_to_string(),
            "مجموع زمان حضور": self.total_time.convert_to_string(),
        }
