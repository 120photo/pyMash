import json, requests

url = 'http://mashable.com/stories.json?new_per_page=60'
data = requests.get(url)
doc = json.loads(data.content)

print(doc)
