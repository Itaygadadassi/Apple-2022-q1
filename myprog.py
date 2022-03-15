#!/usr/bin/env python3


def hello(name: str) -> str:
    return f'Hello, {name}!'


print(hello('world'))
# print(hello(5))
# print(hello(hello))


def mysum(*args: float) -> float:
    total = 0

    for one_arg in args:
        total += one_arg

    return total


print(mysum(10, 20, 30))
print(mysum(10, 'a', 30))
print(mysum(10, 20.5, 30))
