#!/usr/bin/python3
"""
A program that gets a header from a url using urllib
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader("X-Request-Id")
        print(header)
