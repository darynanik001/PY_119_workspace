from Lesson21.open_file import MyOpen
import pytest
import os


@pytest.fixture
def file_obj():
    file_name = "test.txt"
    if os.path.exists(file_name):
        return MyOpen(file_name, "r")
    return MyOpen(file_name, "w")
