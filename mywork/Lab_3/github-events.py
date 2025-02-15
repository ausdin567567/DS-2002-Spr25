#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')

url = 'https://api.github.com/users/{0}/events'.format(GHUSER)

response = requests.get(url)

r = json.loads(response.text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)

