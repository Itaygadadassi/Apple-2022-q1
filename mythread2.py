#!/usr/bin/env python3

import threading
import time
import random


def hello(n):
    time.sleep(random.randint(0, 0))
    print(f'{n} Hello!')


all_threads = []
for i in range(10):
    t = threading.Thread(target=hello, args=(i,))  # run the function in t
    # add the thread to all_threads
    all_threads.append(t)
    t.start()                                      # start the thread

# when we get to this line, all threads should be done

for one_thread in all_threads:
    one_thread.join()           # wait for the thread to finish


print('Done!')
