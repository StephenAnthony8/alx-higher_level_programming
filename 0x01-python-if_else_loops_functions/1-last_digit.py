#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    last_d = int(f"{str(number)[0]}{str(number)[-1]}")
else:
    last_d = int(str(number)[-1])
if (last_d == 0):
    end_output = 0
else:
    end_output = "greater than 5" if (last_d > 5) else "less than 6 and not 0"
print(f"Last digit of {number} is {last_d} and is {end_output}")
