from typing import List


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


if __name__ == "__main__":
    arr = [19, 22, 12, 11, 13, 5, 6]
    insertion_sort(arr)
    print(arr)
