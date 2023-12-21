#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print(0)
    else:
        res = 0
        for i in sys.argv[1:]:
            res += int(i)
        print("{}".format(res))


if __name__ == "__main__":
    main()
