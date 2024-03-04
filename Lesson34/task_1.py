import asyncio
import time


async def calculate_fibonacci(num: int, delay: int):
    a = 0
    b = 1
    c = a + b
    sequence = [a, b, c]
    while num > 0:
        sequence.append(c)
        await asyncio.sleep(delay)
        a, b = b, c
        c = a + b
        num -= 1
    return sequence


async def factorial(num: int, delay: int):
    await asyncio.sleep(delay)
    if num == 1:
        return num
    return num * await factorial(num - 1, delay)


async def squares(num: int, delay: int):
    await asyncio.sleep(delay)
    return num * num


async def cubic(num: int, delay: int):
    await asyncio.sleep(delay)
    return num * num * num


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            calculate_fibonacci(20, 2))

        task2 = tg.create_task(factorial(25, 2))

        task3 = tg.create_task(cubic(234, 2))
        task4 = tg.create_task(squares(234, 2))
        print(f"started at {time.strftime('%X')}")

    print(f"finished at {time.strftime('%X')}")
    print(f"task1 result: {task1.result()}")
    print(f"task2 result: {task2.result()}")
    print(f"task3 result: {task3.result()}")
    print(f"task4 result: {task4.result()}")


if __name__ == "__main__":
    asyncio.run(main())

