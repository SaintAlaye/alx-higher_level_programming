#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD1 = str(number)[-1]
lastD = int(lastD1)

if lastD > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastD))
elif lastD == 0:
    print("Last digit of {} is {} and is 0".format(number, lastD))
elif lastD < 6 and lastD != 0:
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
