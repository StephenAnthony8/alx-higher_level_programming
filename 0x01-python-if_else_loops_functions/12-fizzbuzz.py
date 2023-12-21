#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 100 + 1):
        if (i % 5) and (i % 3):
            print(i, end="")
        if (i % 3 == 0):
            print("Fizz", end="")
        if (i % 5 == 0):
            print("Buzz", end="")

        print("", end=" ")
