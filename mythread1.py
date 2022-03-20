#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')


all_threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))  # run the function in t
    all_threads.append(t)
    t.start()                                      # start the thread

# when we get to this line, all threads should be done


print('Done!')
