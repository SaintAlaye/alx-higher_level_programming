#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD1 = str(number)[-1]
last = int(lastD1)

if last > 5:
    if last > 5 and number < 0:
        print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last < 6 and number != 0:
    if last < 6 and number < 0:
        print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
