#!/bin/bash
# This script displays the size of the body of an HTTP response using curl

# Ensure the script is called with a URL argument
if [ -z "$1" ]; then
    exit 1
fi

# Send a request to the URL and display the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
