from utils import is_prime, NUMBERS
from concurrent.futures import ProcessPoolExecutor
import time


if __name__ == "__main__":
    start = time.time()
    with ProcessPoolExecutor(max_workers=5) as exe:
        for num, is_prime in zip(NUMBERS, exe.map(is_prime, NUMBERS)):
            print(f"Number {num} is prime {is_prime}")
    end = time.time()
    print(f"Whole time: {end - start}")
