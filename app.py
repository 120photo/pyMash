import json, requests

url = 'http://mashable.com/stories.json?new_per_page=60'
data = requests.get(url)
doc = json.loads(data.content)

for story in doc['new']:
    print("""
        ++++++++++++++++++
        Title: {}
        ---
        Excerpt: {}
        ---
        URL: {}

        ++++++++++++++++++""".format(story['title'], story['excerpt'], story['link']))
