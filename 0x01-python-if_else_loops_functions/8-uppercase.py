#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(letter) - uppercase)), end="")
    print()
