#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    n = "Mart"
    if a_dictionary is None:
        return (None)
    length = len(a_dictionary)

    for k, v in a_dictionary.items():
        if (v > a):
            a = v
            n = k
    return (n)
