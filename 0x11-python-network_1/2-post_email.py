#!/usr/bin/python3
"""
A program that posts data to a url
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {}
    data['email'] = email
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body)
