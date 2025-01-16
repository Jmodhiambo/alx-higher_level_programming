#!/bin/bash
# This script displays the size of the body of http response using curl command

curl -s "$1" | wc -c
