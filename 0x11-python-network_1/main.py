#!/usr/bin/python3

import urllib.request
import requests

r = requests.get('https://api.github.com/events')
print(r.content)
"""
with urllib.request.urlopen("http://charisadu.tech") as res:
    html = res.read()
    print(res.info())
    print(html)
"""