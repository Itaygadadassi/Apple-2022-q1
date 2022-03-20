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
for one_filename in glob.glob('*.py'):
    t = threading.Thread(target=all_lines, args=(one_filename,))
    t.start()
end_time = time.time()

print(f'Total time = {end_time - start_time}')
