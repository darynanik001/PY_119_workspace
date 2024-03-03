from concurrent.futures import ThreadPoolExecutor
from utils import is_prime, NUMBERS
import time


if __name__ == "__main__":
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for number, prime in zip(NUMBERS, executor.map(is_prime, NUMBERS)):
            print(F"{number} is prime {prime}")
    end = time.time()

    print(f"Whole time: {end - start}")