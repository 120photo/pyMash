from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template("home.html", doc = doc['new'], categories = categories)

if __name__ == '__main__':
    app.run()
