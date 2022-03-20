#!/usr/bin/env import

from concurrent.futures import ThreadPoolExecutor
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    return f'{n} Hello!'


with ThreadPoolExecutor() as executor:
    all_futures = []
    for i in range(10):
        f = executor.submit(hello, i)
        all_futures.append(f)
