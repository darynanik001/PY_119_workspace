from utils import dump_content, urls
from concurrent.futures import ProcessPoolExecutor
import time


if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.map(dump_content, urls)
    end_time = time.time()
    print(f"Total time: {end_time - start_time}")