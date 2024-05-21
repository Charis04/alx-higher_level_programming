#!/usr/bin/python3
"""
A program that posts data to a url and gets json
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    data = {}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""

    response = requests.post(url, data=data)
    try:
        body = response.json()
        if len(body) == 0:
            print("No result")
        else:
            print(f"[{body[0]['id']}] {body[0]['name']}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
