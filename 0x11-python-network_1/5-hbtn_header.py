#!/usr/bin/python3
"""
A program that gets a header from a url using requests
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    response = requests.get(url)
    header = response.headers.get("X-Request-Id")
    print(header)
