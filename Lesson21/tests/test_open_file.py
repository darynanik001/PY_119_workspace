from Lesson21.open_file import MyOpen
from Lesson21.utils import compress_file
from Lesson21.tests.file_fixtures import file_obj
import unittest
import os


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        self.file_name = "test.txt"
        self.file_modes = ["w", "r", "a"]

    def test_file_exists(self):
        with MyOpen(self.file_name, "w"):
            pass

        self.assertTrue(os.path.isfile(self.file_name), f"File {self.file_name} does not exist.")

    def test_file_not_exists(self):
        with self.assertRaises(FileNotFoundError):
            with MyOpen(self.file_name, "r") as f:
                f.read()

    def test_file_content(self):
        with MyOpen(self.file_name, "w") as f:
            f.write("Hello World!")

        with MyOpen(self.file_name, "r") as f:
            content = f.read()

        self.assertEqual(content, "Hello World!", f"Content is not correct. Expected: Hello World! Got: {content}")

    def test_file_mode(self):
        for mode in self.file_modes:
            with MyOpen(self.file_name, mode) as file:
                self.assertEqual(file.mode, mode, f"File mode is not correct. Expected: {mode}, Got: {file.mode}")

    def tearDown(self):
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


# trying pytest fixture feature
def test_compressed_file_is_exist(file_obj):
    compress_file(file_obj)
    path_to_zip = os.path.abspath(file_obj.file_name + ".zip")
    assert os.path.exists(path_to_zip), f"File {file_obj.file_name}.zip was not created."
    os.remove(path_to_zip)


if __name__ == "__main__":
    unittest.main()
