#!/usr/bin/env python3

import glob


def all_lines(*filenames):
    for one_filename in filenames:
        for one_line in open(one_filename):
            print(one_line)
