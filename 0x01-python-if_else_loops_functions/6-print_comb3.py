#!/usr/bin/python3

for i in range(100):
    if ((f"{i:02d}")[0]) < ((f"{i:02d}")[1]):
        print("{:02d}".format(i), end=", " if i < 89 else "\n")
