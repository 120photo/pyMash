import json, requests


### Variable Declaration ###
url = 'http://mashable.com/stories.json?new_per_page=60'
data = requests.get(url)
doc = json.loads(data.content)

# get channeles
categories = []
# go through all stories and add their channel to the categories list
for story in doc['new']:
    categories.append(story['channel'])
# sort out uniques in list using a set and back to list
categories = sorted(list(set(categories)))

def show_stories():
    for story in doc['new']:
        print("""
            ++++++++++++++++++
            Title: {}
            ---
            Excerpt: {}
            ---
            URL: {}

            ++++++++++++++++++""".format(story['title'], story['excerpt'], story['link']))

# show_stories()
