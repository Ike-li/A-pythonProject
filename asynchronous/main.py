import asyncio


async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def print_letter():
    for i in "abcdefg":
        print(i)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(print_num(), print_letter())


asyncio.run(main())
print("主线程结束！")
