#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = ["+", "-", "*", "/"]
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if "+" in sys.argv[2]:
        value = add(a, b)
    elif "-" in sys.argv[2]:
        value = sub(a, b)
    elif '*' in sys.argv[2]:
        value = mul(a, b)
    elif "/" in sys.argv[2]:
        value = div(a, b)

    print("{} {} {} = {}".format(a, sys.argv[2], b, value))
