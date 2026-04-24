from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

import os
import json

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

CACHE_FILE = "cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

def search_youtube_creators(keyword):
    cache = load_cache()

    if keyword in cache:
        print("⚡ Using cached data")
        return cache[keyword]

    creators = []

    search_req = youtube.search().list(
        q=keyword,
        part="snippet",
        type="channel",
        maxResults=8   # reduced to save quota
    )
    search_res = search_req.execute()

    for item in search_res["items"]:
        channel_id = item["snippet"]["channelId"]

        stats_req = youtube.channels().list(
            part="statistics",
            id=channel_id
        )
        stats_res = stats_req.execute()

        stats = stats_res["items"][0]["statistics"]

        title = item["snippet"]["title"]
        description = item["snippet"]["description"]

        creators.append({
            "name": title,
            "channel_id": channel_id,
            "platform": "YouTube",
            "followers": int(stats.get("subscriberCount", 0)),
            "titles": [title],
            "descriptions": [description],
            "recent_posts": 3
        })

    cache[keyword] = creators
    save_cache(cache)

    return creators