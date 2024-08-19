import asyncio


async def printName(name: str):
    await asyncio.sleep(1)
    print(name)


asyncio.run(printName("Ana Doe"))
