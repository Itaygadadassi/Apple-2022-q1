#!/usr/bin/env import

from concurrent.futures import ThreadPoolExecutor
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    return f'{n} Hello!'
