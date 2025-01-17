#!/usr/bin/python3
# This function returns the peak value in a list or None if empty

def find_peak(list_of_integers):
    """ Returns a peak value from a list"""
    if not list_of_integers:
        return None

    lt = list_of_integers
    length = len(lt)

    # Return the item if it's only in the list
    if length == 1:
        return lt[0]
    # Return the largest value if they are only two
    if length == 2:
        return lt[0] if lt[0] >= lt[1] else lt[1]

    # Finds the mid value to use as starting point
    mid_val = length // 2

    # Boundary checks for mid_value
    if mid_val > 0 and mid_val < length - 1:
        if lt[mid_val] >= lt[mid_val - 1] and lt[mid_val] >= lt[mid_val + 1]:
            return lt[mid_val]
        elif lt[mid_val - 1] > lt[mid_val]:
            return find_peak(lt[:mid_val])  # search in left half
        else:
            return find_peak(lt[mid_val + 1:])  # search in right half
    elif mid_value == 0:  # If the first element is the peak
        if lt[0] >= lt[1]:
            return lt[0]
        else:
            return find_peak(lt[1:])
    else:  # If the last element is the peak
        if lt[-1] >= lt[-2]:
            return lt[-1]
        else:
            return find_peak(lt[:-1])
