#!/usr/bin/python3
"""Fetches the X-Request-Id header from a given URL"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        # Fetch headers
        headers = response.info()
        # Extract the X-Request-Id
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
