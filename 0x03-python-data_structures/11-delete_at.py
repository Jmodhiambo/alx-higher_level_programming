#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    i = 0

    if (idx < 0) or (idx >= length):
        return (my_list)

    for val in my_list:
        if (i == idx):
            del my_list[idx]
        i += 1
    return (my_list)
