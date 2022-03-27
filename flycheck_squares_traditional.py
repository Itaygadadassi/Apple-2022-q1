#!/usr/bin/env python3

from memory_profiler import profile


@profile
def comprehension():
    numbers = range(10_000_000)

    output = []

    for one_number in numbers:
        output.append(one_number ** 2)

    return output


if __name__ == '__main__':

    for i in range(5):
        output = comprehension()
        print(len(output))
