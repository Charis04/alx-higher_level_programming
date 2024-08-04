#!/usr/bin/python3

import requests
import sys

url = f'https://swapi-api.alx-tools.com/api/films/{sys.argv[1]}'

res = requests.get(url)
print(res.json()['title'])
