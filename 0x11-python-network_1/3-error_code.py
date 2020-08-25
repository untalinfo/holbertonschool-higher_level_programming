#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
