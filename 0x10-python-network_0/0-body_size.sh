#!/bin/bash
# This script displays the size of the body of an HTTP response using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
