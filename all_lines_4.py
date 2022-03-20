#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, wait
import queue
import glob
import time


def all_lines(one_filename):
    for one_line in open(one_filename):
        q.put(one_line)


with ThreadPoolExecutor() as executor:
    results = executor.map(all_lines, glob.glob('*.py'))

end_time = time.time()
print(f'Total time = {end_time - start_time}')

# threading: Total time = 0.0012621879577636719
# serial:  = Total time = 0.0006771087646484375
# executor:  Total time = 0.0044422149658203125
