#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for i in names:
        if "__" not in i:
            print(i)


if __name__ == "__main__":
    main()
