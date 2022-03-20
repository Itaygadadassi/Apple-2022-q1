#!/usr/bin/env python3

import threading
import queue
import glob
import time


q = queue.Queue()


def all_lines(one_filename):
    for one_line in open(one_filename):


def all_lines(*filenames):
    for one_filename in filenames:
        for one_line in open(one_filename):
            print(one_line)


start_time = time.time()
all_lines(*glob.glob('*.py'))
end_time = time.time()

print(f'Total time = {end_time - start_time}')
