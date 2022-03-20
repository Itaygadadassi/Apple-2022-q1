#!/usr/bin/env python3

import glob
import time


def all_lines(*filenames):
    for one_filename in filenames:
        for one_line in open(one_filename):
            print(one_line)


start_time = time.time()
all_lines(*glob.glob('*.py'))
end_time = time.time()

print(f'Total time = {end_time - start_time}')
