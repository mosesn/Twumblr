from pymongo import Connection
import requests
import json

conn = Connection()
users = conn.db.users

names = users.find()



for sn in names:
    lst = json.loads(requests.get("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=mnnakamura").content)
    
