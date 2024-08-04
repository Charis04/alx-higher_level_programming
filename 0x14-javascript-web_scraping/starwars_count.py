#!/usr/bin/python3

import requests
import sys

url = sys.argv[1]
character = 'https://swapi-api.alx-tools.com/api/people/18/'

res = requests.get(url)
films = res.json()['results']
count = 0
for film in films:
    if character in film['characters']:
        count += 1

print(count)
