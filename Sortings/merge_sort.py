from typing import List
from random import shuffle


def sort(arr: List[int], left: List[int], right: List[int]):
    m = len(left)
    n = len(right)

    i = j = k = 0
    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1

    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1


def merge_sort(lst: List[int]):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = [lst[x] for x in range(mid)]
        right = [lst[y] for y in range(mid, len(lst))]

        merge_sort(left)
        merge_sort(right)

        sort(lst, left, right)


if __name__ == "__main__":
    ll = [a for a in range(10)]
    shuffle(ll)
    print(f"Before sorting: {ll}")
    merge_sort(ll)
    print(f"After sorting: {ll}")
