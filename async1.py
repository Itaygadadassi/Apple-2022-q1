#!/usr/bin/env python3

import asyncio


# function that I want to run in the asyncio "event loop"
# the function is run indirectly, via the event loop
# it'll run until (a) it ends or (b) it says await, in which case it goes to sleep (similar to yield)
async def hello(n):
    print(f'{n} Hello!')
    await asyncio.sleep(1)
    print(f'{n} Goodbye!')


# here, I use "await" to say: I'm waiting for hello to run
# but here, things don't run in parallel
async def main():
    for i in range(5):
        await hello(i)

asyncio.run(main())   # run our async def function
