#!/usr/bin/python3
""" Fetch URLs"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()
try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("    - type:", type(body))
        print("    - content:", body)
        print("    - utf8 content:", body.decode('utf-8'))
except Exception as e:
    print("Error:", e)
