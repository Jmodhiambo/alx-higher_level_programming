#!/usr/bin/python3
# This function returns the peak value in a list or None if empty

def find_peak(list_of_integers):
    """ Returns a peak value from a list"""

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_idx = int(len(list_of_integers) / 2)

    if mid_idx != len(list_of_integers) - 1:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
           list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
    else:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
        else:
            return list_of_integers[mid_idx - 1]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        a_list = list_of_integers[0:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)

"""
def find_peak(list_of_integers):
    "" Returns a peak value from a list""
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
            return find_peak(lt[:-1])"""
