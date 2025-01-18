#!/usr/bin/python3
"""Fetches the X-Request-Id header from a given URL"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    # Extract the X-Request-Id
    print(response.headers['X-Request-Id'])
