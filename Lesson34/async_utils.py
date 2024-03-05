import json
import asyncio
import aiohttp
from typing import List

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


async def sort_content_by_date(content: List[dict], delay: float) -> None:
    await asyncio.sleep(delay)
    content.sort(key=lambda item: item["date"])


async def get_content(url: str, session) -> List[dict]:
    async with session.get(url, ssl=False) as response:
        data = await response.json()
        return data


async def dump_content(url: str, session) -> None:
    content = await get_content(url, session)
    await sort_content_by_date(content, .5)
    with open("data.json", "a") as f:
        json.dump(content, f, indent=2)
