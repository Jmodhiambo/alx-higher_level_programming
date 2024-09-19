#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0

    for k, v in my_list:
        score += (k * v)
        weight += v

    return (score/weight)
