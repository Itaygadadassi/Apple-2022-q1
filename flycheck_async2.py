#!/usr/bin/env python3

import asyncio
import time


# function that I want to run in the asyncio "event loop"
# the function is run indirectly, via the event loop
# it'll run until (a) it ends or (b) it says await, in which case it goes to sleep (similar to yield)
async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)      # await needs an "awaitable"
    print(f'{n} Goodbye!')


# instead of using "await", we'll use "create_task" to add the function
# to the event loop.
async def main():

    # add these three tasks to the event loop

    t1 = asyncio.create_task(hello(1))
    t2 = asyncio.create_task(hello(2))
    t3 = asyncio.create_task(hello(3))

    await t1b  
    await t2
    await t3

    await t1
    await t2
    await t3


asyncio.run(main())   # run our async def function
