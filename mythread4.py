#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    return f'{n} Hello!'


with ThreadPoolExecutor(max_workers=20) as executor:
    all_results = executor.map(hello, range(10))

    for one_result in all_results:
        print(one_result)
