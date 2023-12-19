import re


def count_lines(file_cursor):
    file_cursor.seek(0)
    return len(file_cursor.readlines())


def count_chars(file_cursor):
    counter = 0
    file_cursor.seek(0)
    for line in file_cursor.read():
        if re.match(r"[a-zA-Z]", line):
            counter += 1
    return counter


def test(name):
    with open(name, "r") as f:
        num_of_lines = count_lines(f)
        num_of_chars = count_chars(f)
        print(num_of_lines, num_of_chars, name)


__all__ = ("test",)
