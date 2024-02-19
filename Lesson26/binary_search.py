from typing import List


def binary_search_recursive(array: List, element: int) -> bool:
    mid = len(array) // 2

    if element in arr:
        if array[mid] == element:
            return True

        if array[mid] > element:
            return binary_search_recursive(array[0:mid], element)

        if array[mid] < element:
            return binary_search_recursive(array[mid+1:], element)

    return False


def binary_search_iterative(array: List, element: int) -> bool:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if element == array[mid]:
            return True

        if element < array[mid]:
            high = mid - 1

        if element > array[mid]:
            low = mid + 1
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search_recursive(arr, -565))
    print(binary_search_iterative(arr, 9))