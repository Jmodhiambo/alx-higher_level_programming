#!/usr/bin/python3
# This function returns the peak value in a list or None if empty

def find_peak(list_of_integers):
    """Returns a peak value from a list"""
    if not list_of_integers:
        return None

    lt = list_of_integers
    length = len(lt)

    # Return the item if it's the only element in the list
    if length == 1:
        return lt[0]
    # Return the largest value if there are only two elements
    if length == 2:
        return lt[0] if lt[0] >= lt[1] else lt[1]

    # Find the mid value to use as the starting point
    mid_value = length // 2

    # Check for peak at mid_value
    if (mid_value > 0 and lt[mid_value] >= lt[mid_value - 1]) and\
       (mid_value < length - 1 and lt[mid_value] >= lt[mid_value + 1]):
        return lt[mid_value]

    # If left neighbor is greater, search the left half
    if mid_value > 0 and lt[mid_value - 1] > lt[mid_value]:
        return find_peak(lt[:mid_value])  # search in left half

    # If right neighbor is greater, search the right half
    return find_peak(lt[mid_value + 1:])  # search in right half
