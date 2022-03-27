#!/usr/bin/env python3

import asyncio


async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)
    print(f'{n} Goodbye!')


async def main():
    for i in range(5):
        await hello(i)

asyncio        