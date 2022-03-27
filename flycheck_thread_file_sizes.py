#!/usr/bin/env python3

import threading
import glob
import os


def file_size(filename):
    return filename, os.stat(filename).st_size

