#!/usr/bin/env python3

import asyncio


# function that I want to run in the asyncio "event loop"
async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)
    print(f'{n} Goodbye!')


async def main():
    for i in range(5):
        await hello(i)

asyncio.run(main())   # run our async def function
