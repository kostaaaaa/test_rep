import asyncio
import time


async def square(number: int):
    await asyncio.sleep(3)
    print(number**2)

async def cube(number: int):
    await asyncio.sleep(3)
    print(number**3)

async def main():
    task1 = asyncio.create_task(
        square(4))

    task2 = asyncio.create_task(
        cube(2))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
