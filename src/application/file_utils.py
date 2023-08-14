from os import mkdir


class File_Utils:
    @staticmethod
    def create_folder(path: str, name: str) -> None:
        try:
            mkdir(f"{path}\\{name}")

        except Exception:
            pass

    @staticmethod
    def list_of_dictionary_to_text_file(
        items: list[dict], file_name: str, separator: str = " "
    ) -> None:
        File_Utils.create_folder(path=".\\", name="dist")

        text_file = open(f"dist\\{file_name}.txt", "w", encoding="utf-8")

        for item in items:
            line = ""

            for key in item:
                line += f"{item[key]}{separator}"

            text_file.write(f"{line}\n")
