#!/usr/bin/python3
"""Takes in a URL, send a request to it, and display the value of
the x-Request-Id
"""
import urllib.request
import sys

if '__main__' == '__name__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(f"{x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLErro as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nRequest canceled by the user.")
