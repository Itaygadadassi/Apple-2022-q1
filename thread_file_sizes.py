#!/usr/bin/env python3

import threading
import glob
import os


def file_size(filename):
    return filename, os.stat(filename).st_size


for one_filename in glob.glob('/etc/*'):
    t = threading.Thread(target=file_size, args=(one_filename,))
    t.start()
