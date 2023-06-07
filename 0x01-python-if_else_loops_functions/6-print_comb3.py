#!/usr/bin/python3

for numbers in range(0, 10):
    for number in range(numbers + 1, 10):
            if numbers * 10 + number < 89:
                print("{:02d}".format(numbers * 10 + number), end=", ")
            else:
                print("{:02d}".format(numbers * 10 + number))
