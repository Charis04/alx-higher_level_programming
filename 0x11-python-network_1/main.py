#!/usr/bin/python3

import urllib.request
import requests

r = requests.get('https://api.github.com/events')
try:
    print(int(r.content))
except:
    print("Error")
"""
with urllib.request.urlopen("http://charisadu.tech") as res:
    html = res.read()
    print(res.info())
    print(html)
"""