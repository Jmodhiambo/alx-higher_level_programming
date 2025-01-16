#!/bin/bash
# This script displays the size of the body of an HTTP response using curl
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
