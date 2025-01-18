#!/usr/bin/python3
"""This script sends a request to the URL and displays response's body"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Check if the error code 400 and above
    if int(response.status_code) >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
