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
    return f'Done from {n}'


# instead of using "await", we'll use "create_task" to add the function
# to the event loop.
async def main():

    # create a list of tasks, each of which is on the event loop
    tasks = [asyncio.create_task(hello(n))
             for n in range(5)]

    # wait until all tasks are done running on the event loop
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())   # run our async def function
