#!/usr/bin/python3
def uppercase(str):

    for i in str:
        ascii_num = ord(i)

        if (ascii_num >= 97) and (ascii_num <= 122):
            ascii_num = ascii_num - 32
            i = chr(ascii_num)

        print("{}".format(i), end="")

    print("\n", end="")
