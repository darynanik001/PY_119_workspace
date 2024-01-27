from typing import TextIO
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MyOpen:

    def __init__(self, full_file_name, *args, **kwargs):
        self.full_file_name = full_file_name
        self.file = open(full_file_name, *args, **kwargs)
        self._counter = 0
        logger.info(f"{self.file_name} is opened in mode {self.file.mode}, counter {self._counter}")

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def file_name(self) -> str:
        return self.full_file_name.split(".")[0]

    def __enter__(self) -> TextIO:
        self._counter += 1
        logger.info(f"Entering runtime context, counter value: {self._counter}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._counter -= 1
        self.file.close()
        logger.info(f"Exited runtime context of {self.file_name}, counter value: {self._counter}")

    def close(self):
        self._counter -= 1
        self.file.close()
        logger.info(f"Closing file {self.file_name}, counter value: {self._counter}")


if __name__ == "__main__":
    with MyOpen("test.txt", "w") as write_file:
        write_file.write("hello")
        with MyOpen("tes.txt") as read_file:
            print(read_file.read())
