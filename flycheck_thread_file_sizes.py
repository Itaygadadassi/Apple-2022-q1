#!/usr/bin/env python3

import threading
import glob
import os

# from Python 3.8, we can do this:


def handle_exception(*args):
    print(f'Exception: {args}')


threading.excepthook = handle_exception


def file_size(filename):
    return filename, os.stat(filename).st_size


for one_filename in glob.glob('/etc/*'):
    print(one_filename)
    t = threading.Thread(target=file_size, args=(one_filename,))
    t.start()
