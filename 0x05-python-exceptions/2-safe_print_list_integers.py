#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip if it's not an integer
            continue
        except IndexError:
            # Stop if the index is out of range
            break
    print()  # Print a new line after the loop
    return count
