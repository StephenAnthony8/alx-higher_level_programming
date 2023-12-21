#!/usr/bin/python3
"""
    101-stats.py
    - contains metrics_compute function
"""
import sys
from time import sleep
import random


def metrics_compute():
    """
        metrics_compute
        - calculates metrics from given input
        - tallies the number of http status codes that it recieves
    """
    count = 0
    stat_codes = {'200': 0,
                  '301': 0,
                  '400': 0,
                  '401': 0,
                  '403': 0,
                  '404': 0,
                  '405': 0,
                  '500': 0}

    code_cpy = stat_codes.copy()
    f_size = 0
    while (True):
        try:
            line = input()

            lines = (line.strip()).split(" ")
            code_str = lines[-2]
            f_size += int(lines[-1])
            if code_str in code_cpy.keys():
                code_cpy[code_str] += 1

            if (count % 10) == 0 and (count > 0):
                print("File size: {:d}".format(f_size))
                for key in code_cpy:
                    if code_cpy[key] != 0:
                        print("{}: {}".format(key, code_cpy[key]))

                code_cpy = stat_codes.copy()

        except (EOFError, KeyboardInterrupt) as e:
            print('File size: {:d}'.format(f_size))
            for key in code_cpy:
                if code_cpy[key] != 0:
                    print("{}: {}".format(key, code_cpy[key]))
                    raise

        count += 1


def main():
    metrics_compute()


if __name__ == "__main__":
    main()
