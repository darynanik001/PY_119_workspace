from typing import List
from random import shuffle
from insertion_sort import insertion_sort
from time import time


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__} took {end - start} seconds')
    return wrapper


def partition(array: List[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


@time_count
def quicksort(array: List[int], low: int, high: int, partition_limit=50):
    if partition_limit < partition_limit:
        insertion_sort(array)
    else:
        if low < high:
            pi = partition(array, low, high)
            quicksort(array, low, pi - 1)
            quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
    array = [x for x in range(10)]
    shuffle(array)
    quicksort(array, 0, len(array)-1, 8)
    print("Sorted array")
    print(array)
