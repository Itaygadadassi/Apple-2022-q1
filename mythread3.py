#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    return f'{n} Hello!'


with ThreadPoolExecutor(max_workers=2) as executor:
    all_futures = []
    for i in range(10):
        f = executor.submit(hello, i)
        all_futures.append(f)

    done, not_done = wait(all_futures)

    for one_item in done:
        print(one_item.result())
