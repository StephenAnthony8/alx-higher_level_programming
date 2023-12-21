#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    signs = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    sign = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sign == "+":
        res = add(a, b)
    elif sign == "-":
        res = sub(a, b)
    elif sign == "*":
        res = mul(a, b)
    elif sign == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, sign, b, res))


if __name__ == "__main__":
    main()
