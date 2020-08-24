#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
from os import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.headers['X-Request-Id']
        print(value)
