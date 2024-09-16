#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    fin_string = list()
    deli = ""
    for i in new_string:
        if (i == 'c') or (i == 'C'):
            continue
        fin_string.append(i)
    fin = deli.join(fin_string)
    return (fin)
