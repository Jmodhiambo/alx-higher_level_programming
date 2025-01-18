#!/usr/bin/python3
"""Fetches GitHub user ID using Basic Authentication with a PAT"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # Prepare the authentication tuple (username, personal access token)
    auth = (username, token)

    # Make the GET request to GitHub API to fetch user information
    response = requests.get("https://api.github.com/user", auth=auth)

    if response.status_code == 200:
        # If the request was successful, display the user ID
        user_info = response.json()
        print(user_info.get("id"))
    else:
        # If the authentication fails or any other error occurs, print None
        print(None)
