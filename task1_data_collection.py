import requests
import json
import os
import time
from datetime import datetime

top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"
headers = {
    "User-Agent": "TrendPulse/1.0"
}

# keywords for each category
category_keywords = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}
def find_category(title):
    title = title.lower()
    for category in category_keywords:
        for word in category_keywords[category]:
            if word in title:
                return category
    return None
  
#step 1:top story apply
try:
    response = requests.get(top_stories_url, headers=headers)
    story_ids = response.json()
except:
    print("Error while fetching top stories")
    story_ids = []
story_ids = story_ids[:500]
all_stories = []
category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

#step 2:fetch each story
for story_id in story_ids:
    try:
        res = requests.get(item_url.format(story_id), headers=headers)
        story = res.json()
    except:
        print("Failed to fetch story:", story_id)
        continue
    if story is None:
        continue
    if "title" not in story:
        continue
    title = story["title"]
    category = find_category(title)
    if category is None:
        continue
    if category_count[category] >= 25:
        continue
    one_story = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by", "unknown"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    all_stories.append(one_story)
    category_count[category] += 1
    done = True
    for cat in category_count:
        if category_count[cat] < 25:
            done = False
            break
    if done:
        break
time.sleep(2)

#step 3:save JSON
if not os.path.exists("data"):
    os.makedirs("data")
file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(all_stories, f, indent=4)
print("Collected", len(all_stories), "stories. Saved to", file_name)
