#!/usr/bin/env python3

from memory_profiler import profile


@profile
def comprehension():
    numbers = range(10_000_000)

    return [one_number ** 2
            for one_number in numbers]


for i in range(5):
    output = comprehension()
    print(len(output))
