#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenght = -(len(my_list))
    i = -1
    while (i >= lenght):
        print("{:d}".format(i))
        i = i - 1
