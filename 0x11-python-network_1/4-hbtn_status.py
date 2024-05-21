#!/usr/bin/python3
import requests

url = "https://alx-intranet.hbtn.io/status"

res = requests.get(url)

print("Body response:")
print("\t- type:", type(res))
print("\t- content:", res.content)
print("\t- utf8 content:", res.text)
