#!/usr/bin/python3
"""
Sends a POST request with a letter as a parameter
   and processes the JSON response
"""

import requests
import sys

if __name__ == "__main__":
    # Check if an argument was provided, otherwise set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send the POST request with the letter as parameter 'q'
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        if json_response:
            # If the JSON is not empty, print id and name
            print(f"[{json_response.get("id")}] {json_response.get("name")")
        else:
            # If the JSON is empty, print "No result"
            print("No result")
    except ValueError:
        # If the response is not valid JSON, print "Not a valid JSON"
        print("Not a valid JSON")
