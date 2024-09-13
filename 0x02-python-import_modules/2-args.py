#!/usr/bin/python3
import sys

if __name__ == "__main__":

    l = len(sys.argv) -  1
    list = sys.argv[1:]

    if (l == 0):
        print("0 arguments.")

    elif (l == 1):
        print(f"{l} argument:\n1: {list[0]}")

    else:
        print(f"{l} arguments:")
        for i in range(l):
            print(f"{i + 1}: {list[i]}")
