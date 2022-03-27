#!/usr/bin/env python3

@profile
def comprehension():
    numbers = range(10_000_000)

    output = []

    for one_number in numbers:
        output.append(one_number ** 2)

    return output


for i in range(5):
    output = comprehension()
    print(len(output))
