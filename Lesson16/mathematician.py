from typing import List


class Mathematician:
    def __init__(self):
        pass

    @staticmethod
    def square_nums(nums: List):
        return list(map(lambda x: x ** 2, nums))

    @staticmethod
    def remove_positives(nums: List):
        return list(filter(lambda x: x < 0, nums))

    @staticmethod
    def filter_leaps(years: List):
        leap_years = []

        for year in years:
            if year % 4 == 0:
                if year % 100 != 0 or year % 400 == 0:
                    leap_years.append(year)
        return leap_years


if __name__ == "__main__":
    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
