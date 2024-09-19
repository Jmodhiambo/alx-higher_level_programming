#!/usr/bin/python3
def best_score(a_dictionary):
    a = None
    n = None
    if a_dictionary is None:
        return (None)
    length = len(a_dictionary)

    for k, v in a_dictionary.items():
        if a is None or v > a:
            a = v
            n = k
    return (n)
