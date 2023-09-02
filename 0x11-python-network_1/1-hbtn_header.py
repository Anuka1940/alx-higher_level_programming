#!/usr/bin/python3
"""Takes in a URL, send a request to it, and display the value of
the x-Request-Id
"""
import urllib.request
import sys

if '__main__' == '__name__':
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
