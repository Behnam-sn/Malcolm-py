class Date_Utils:
    @staticmethod
    def number_to_string(number: int) -> str:
        string = str(number)

        if len(string) == 1:
            string = f"0{string}"

        return string
