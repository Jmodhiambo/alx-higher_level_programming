#!/usr/bin/python3
"""Fetches the 10 most recent commits of a repository from a specific owner."""

import requests
import sys

if __name__ == "__main__":
    # Extract repository name and owner name from the arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the GitHub API URL
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        # Make the GET request to fetch commits
        response = requests.get(url)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        commits = response.json()

        # Print the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
