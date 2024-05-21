#!/usr/bin/python3
"""
A program that sends request to a url and prints error code if any
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        body = response.text
        print(body)
    else:
        print('Error code:', response.status_code)
