#!/usr/bin/python3
import sys

if __name__ == "__main__":

    length = len(sys.argv) - 1
    args = sys.argv[1:]
    ssum = 0

    for i in args:
        ssum = ssum + int(i)
    print(ssum)
