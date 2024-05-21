#!/usr/bin/python3
"""
A program that posts data to a url
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {}
    data['email'] = email

    response = requests.post(url, data=data)
    body = response.text
    print(body)
