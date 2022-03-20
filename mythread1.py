#!/usr/bin/env python3

import threading


def hello():
    print('Hello!')


for i in range(10):
    t = threading.Thread(target=hello)  # when started, run the function in t
    t.start()                           # start the thread
