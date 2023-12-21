#!/usr/bin/python3
import sys


def main():
    arg_c = len(sys.argv) - 1

    arguments = "arguments" if arg_c != 1 else "argument"
    punct = ":" if arg_c > 0 else "."
    print("{} {}{}".format(arg_c, arguments, punct))
    if (arg_c > 0):
        for i in range(1, arg_c + 1):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
