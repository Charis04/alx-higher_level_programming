#!/usr/bin/python3
"""
A program that sends request to a url and prints error code if any
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
