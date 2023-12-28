import time
from typing import Any


def func(arg1: Any, arg2: Any):
    t = time.time()
    string = "hello"


def count_locals(f):
    """Write a Python program to detect the number of local variables declared in a function."""
    return f.__code__.co_nlocals


def generate_power(exp: int):
    """Write a Python program to access a function inside a function (Tips: use function, which returns another
    function)"""
    def power(item: int):
        return item ** exp

    return power


def choose_func(nums: list, func1, func2):
    """Write a function called "choose_func" which takes a list of nums and 2 callback functions. If all nums inside
    the list are positive, execute the first function on that list and return the result of it. Otherwise,
    return the result of the second one"""
    if all(tuple(map(lambda x: x > 0, nums))):
        return func1(nums)
    return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == "__main__":
    print(count_locals(func))
    power_item = generate_power(3)
    print(power_item(4))

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
