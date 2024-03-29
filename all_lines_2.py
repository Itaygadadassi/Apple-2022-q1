#!/usr/bin/env python3

import threading
import queue
import glob
import time


q = queue.Queue()


def all_lines(one_filename):
    for one_line in open(one_filename):
        q.put(one_line)


start_time = time.time()
all_threads = []
for one_filename in glob.glob('*.py'):
    t = threading.Thread(target=all_lines, args=(one_filename,))
    all_threads.append(t)
    t.start()

for one_thread in all_threads:
    one_thread.join()
end_time = time.time()

while not q.empty():
    print(q.get())

print(f'Total time = {end_time - start_time}')


# threading: Total time = 0.0012621879577636719
# serial:  = Total time = 0.0006771087646484375
9
