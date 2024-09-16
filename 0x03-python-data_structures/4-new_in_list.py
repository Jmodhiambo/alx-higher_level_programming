#!/usr/bin/python
def new_in_list(my_list, idx, element):

    length = len(my_list)
    if (idx < 0) or (idx >= length):
        return (my_list[:])

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
