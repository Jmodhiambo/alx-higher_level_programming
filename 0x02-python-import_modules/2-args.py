#!/usr/bin/python3
import sys

if __name__ == "__main__":

    length = len(sys.argv) - 1
    list = sys.argv[1:]

    if (length == 0):
        print("0 arguments.")

    elif (length == 1):
        print(f"{length} argument:\n1: {list[0]}")

    else:
        print(f"{length} arguments:")
        for i in range(length):
            print(f"{i + 1}: {list[i]}")
