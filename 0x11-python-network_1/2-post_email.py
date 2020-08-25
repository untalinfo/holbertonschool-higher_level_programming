#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
from os import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
