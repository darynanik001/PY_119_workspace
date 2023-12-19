# from mod_1 import get_random_between
import mod_1

from sys import path

# path[0] = "hello"
# from mod_1 import import get_random_between # impossible to import after path[0] = hello

# Task 1
# print("Random number:", get_random_between(10, 100))

def test():
    try:
        1/0
    except ZeroDivisionError:
        return 1
    finally:
        return 0


if __name__ == "__main__":
    print(test())