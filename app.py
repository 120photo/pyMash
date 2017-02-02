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

def categories_menu():
    print("Welcome / Read Mashable Stories")
    print("Select a Category for Stories")
    for index, category in enumerate(categories):
        print("{} : {}".format(index,category))
    print("{} : All".format(len(category) + 1))

categories_menu()
user_choice = input("Choose a number : ")
# show_stories()
