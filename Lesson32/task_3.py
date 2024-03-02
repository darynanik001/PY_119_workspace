from typing import Callable
import requests
import threading
import shutil

status_codes = [
    100, 101, 102, 103,
    200, 201, 202, 203, 204, 205, 206, 207, 208,
    300, 301, 302, 303, 304, 305, 306, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408,
    500, 501, 502, 503, 504, 506, 507, 508, 509
]


def thread_pool_executer(func: Callable, num_of_threads: int, *args) -> list:
    for _ in range(num_of_threads):
        thread = threading.Thread(target=func, args=args)
        yield thread


def make_request_and_save_content(url: str, status_code: str) -> None:
    response = requests.get(url, stream=True)
    with open(f"images/{status_code}.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)


if __name__ == "__main__":
    threads = []
    for status_code in status_codes:
        url = f"https://http.cat/{status_code}"

        for thread in thread_pool_executer(make_request_and_get_content, 3, url, str(status_code)):
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()