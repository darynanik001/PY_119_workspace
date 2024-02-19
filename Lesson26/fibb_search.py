from typing import List


def fib_search(arr: List, x: int, n: int) -> bool:
    fib_k1 = 0
    fib_k2 = 1
    fib_k = fib_k1 + fib_k2

    # fib_k is going to store the smallest
    # Fibonacci Number greater than or equal to n
    while fib_k < n:
        fib_k1 = fib_k2
        fib_k2 = fib_k
        fib_k = fib_k1 + fib_k2

    offset = -1

    if arr[n - 1] == x:
        return n - 1

    while fib_k > 1:

        # Check if fib_k2 is a valid location
        i = min(offset + fib_k1, n - 1)

        # If x is greater than the value at
        # index fib_k1, cut the subarray array
        # from offset to i
        if arr[i] < x:
            fib_k = fib_k2
            fib_k2 = fib_k1
            fib_k1 = fib_k - fib_k1
            offset = i

        # If x is less than the value at
        # index fib_k2, cut the subarray
        # after i+1
        elif arr[i] > x:
            fib_k = fib_k1
            fib_k2 = fib_k2 - fib_k1
            fib_k1 = fib_k1 - fib_k2

        # element found
        else:
            return True

    # element not found
    return False


if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]
    n = len(arr)
    x = 82
    index = fib_search(arr, x, n)
    print(index)