import json

import requests

import secrets

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + secrets.GCLOUD_TOKEN,
}

data = {
  'target': 'en',
  'format': 'text'
}

with open('to_translate.txt') as f:
  text = f.read()

url = "https://translation.googleapis.com/language/translate/v2"
results = []
lines = text.splitlines()
for i, line in enumerate(lines):
  print("translating {}/{}: {}".format(i + 1, len(lines), line))
  data['q'] = line
  resp = requests.post(url, headers=headers, data=json.dumps(data))
  results.append(resp.json())

with open('translation_results.json', 'w') as f:
  f.write(json.dumps(results, indent=2))
