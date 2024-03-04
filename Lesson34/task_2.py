from async_utils import dump_content, urls
import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for url in urls:
                tg.create_task(dump_content(url, session))


if __name__ == "__main__":
    asyncio.run(main())
