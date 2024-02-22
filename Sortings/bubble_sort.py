from typing import List
from time import time
from random import shuffle


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__} took {end - start} seconds')

    return wrapper


@time_count
def bubble_sort_even_odd(lst: List[int]):
    size = len(lst)

    for i in range(size):
        if i % 2 == 0:
            for j in range(1, size, 2):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
        else:
            for j in range(1, size - 1, 2):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]


@time_count
def bubble_sort_in_both_directions(lst: List[int]):
    size = len(lst)
    start = 0
    end = size - start - 1
    while start < end:

        for j in range(start, end):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

        end -= 1

        for j in range(end, start, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        start += 1


@time_count
def bubble_sort(lst: List[int]):
    size = len(lst)

    for i in range(size):
        for j in range(size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == "__main__":
    #
    ll = [r for r in range(1000)]
    # 3 5 9 8 12 34
    shuffle(ll)
    print(ll)
    # bubble_sort_even_odd(ll)
    #bubble_sort(ll)
    bubble_sort_in_both_directions(ll)
    print("Sorted", ll)
