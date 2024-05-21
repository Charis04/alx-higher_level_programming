#!/usr/bin/python3
"""
Program that sends request using requests lib
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
