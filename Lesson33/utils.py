from typing import List
import math
import requests
import json


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(n ** .5))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

urls = [
    "https://date.nager.at/api/v2/publicholidays/2024/US",
    "https://date.nager.at/api/v2/publicholidays/2024/AD",
    "https://date.nager.at/api/v2/publicholidays/2024/AL",
    "https://date.nager.at/api/v2/publicholidays/2024/CZ",
    "https://date.nager.at/api/v2/publicholidays/2024/GB",
    "https://date.nager.at/api/v2/publicholidays/2024/PL",
    "https://date.nager.at/api/v2/publicholidays/2024/AT",
    "https://date.nager.at/api/v2/publicholidays/2024/CO",
    "https://date.nager.at/api/v2/publicholidays/2024/CH",
]


def sort_content_by_date(content: List[dict]) -> None:
    content.sort(key=lambda item: item["date"])


def get_content(url: str) -> List[dict]:
    response = requests.get(url)
    return response.json()


def dump_content(url: str) -> None:
    content = get_content(url)
    sort_content_by_date(content)
    with open("data.json", "w") as f:
        json.dump(content, f, indent=2)