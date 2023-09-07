#!/usr/bin/python3
""" Takes a URL as input, send a POST request and display the response"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            res_body = response.read().decode('utf-8')
            print(res_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
