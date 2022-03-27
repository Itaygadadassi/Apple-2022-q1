#!/usr/bin/env python3

import threading
import time

l = threading.Lock()


def write_to_log(id_number):
    for i in range(10):
        with open(f'log.txt', 'a') as f:
            for j in range(5):
                time.sleep(0.1)
                f.write(f'{i} Log {id_number} line {j}\n')


for thread_id in range(5):
    t = threading.Thread(target=write_to_log, args=(thread_id,))
    t.start()
