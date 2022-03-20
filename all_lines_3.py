#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import queue
import glob
import time

q = queue.Queue()


def all_lines(one_filename):
    for one_line in open(one_filename):
        q.put(one_line)


with ThreadPoolExecutor(max_workers=20) as executor:
    all_futures = []
    start_time = time.time()
    for one_filename in glob.glob('*.py'):
        one_future = executor.submit(all_lines, one_filename)
        all_futures.append(one_future)

    done, not_done = wait(all_futures)


while not q.empty():
    print(q.get())

end_time = time.time()
print(f'Total time = {end_time - start_time}')

# threading: Total time = 0.0012621879577636719
# serial:  = Total time = 0.0006771087646484375
# executor:  Total time = 0.0044422149658203125
