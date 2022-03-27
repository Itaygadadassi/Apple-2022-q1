#!/usr/bin/env python3

import threading


def write_to_log(id_number):
    for i in range(10):
        with open(f'log.txt', 'a') as f:
            for j in range(5):
                f.write('{i} Log {id_number} line {j}\n')


for thread_id in range(5):
    t = threading.Thread(target=write_to_log, args=(thread_id,))
    t.start()
