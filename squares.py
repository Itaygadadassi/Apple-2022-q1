#!/usr/bin/env python3

def comprehension():
    numbers = range(10_000_000)

    return [one_number ** 2
            for one_number in numbers]


timeit.timeit('traditional_loop()', number=3, globals=globals())
