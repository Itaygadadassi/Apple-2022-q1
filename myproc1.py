#!/usr/bin/env python3

import multiprocessing
import time
import random
import queue


q = multiprocessing.Queue()


def hello(n):
    time.sleep(random.randint(0, 3))
    q.put(f'{n} Hello!')


all_processes = []
for i in range(10):
    p = multiprocessing.Process(
        target=hello, args=(i, q))
    all_processes.append(p)
    p.start()                                      # start the thread

# when we get to this line, all threads should be done

for one_process in all_processes:
    one_process.join()           # wait for the thread to finish


print('Done!')

while not q.empty():
    print(q.get())
