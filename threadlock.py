#!/usr/bin/env python3

def write_to_log(id_number):
    for i in range(10):
        with open(f'log.txt', 'a') as f:
            for j in range(5):
                f.write('{i} Log {id_number} line {j}\n')
