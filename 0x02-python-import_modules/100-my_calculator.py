#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    length = len(sys.argv) - 1
    a = int(args[0])
    opr = args[1]
    b = int(args[2])

    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if (opr == '+') or (opr == '-') or (opr == '*') or (opr == '/'):
        if (opr == '+'):
            print("{} {} {} = {}".format(a, opr, b, add(a, b)))
            exit(0)

        elif (opr == '-'):
            print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
            exit(0)

        elif (opr == '*'):
            print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
            exit(0)

        else:
            print("{} {} {} = {}".format(a, opr, b, div(a, b)))
            exit(0)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
