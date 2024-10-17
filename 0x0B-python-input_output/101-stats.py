#!/usr/bin/python3
"""
This script reads from standard input line by line and computes metrics:
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated total file size and the count of each status code.

    Args:
        total_size (int): The total size of all files processed.
        status_codes (dict):
            A dictionary containing the counts of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Initialize variables
total_size = 0
line_count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            # The file size is the last part of the line
            total_size += int(parts[-1])

            # The status code is the second-to-last part of the line
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            # If there's an issue parsing the line, skip it
            pass

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    # Print the final statistics upon interruption
    print_stats(total_size, status_codes)
    raise

# Print the final statistics after reading all lines
print_stats(total_size, status_codes)
