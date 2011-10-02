#!/usr/bin/env python

import sys
import time
import signal
import json
import requests
from pymongo import Connection
from tumblr import TumblrClient
import oauth2

#conn = Connection("mongodb://root:u4URSQ0KGiNubhrq1ab4@twumblr-bakanaka-data-0.dotcloud.com:14914")
#coll = conn.db.users()

# Callback called when you run `supervisorctl stop'
def sigterm_handler(signum, frame):
    print >> sys.stderr, "Kaboom Baby!"
    sys.exit(0)

def tumble(stri, tumcli):
    if stri.find("t.co") != -1:
        for text in stri.split():
            if text.find("t.co") != -1:
                r = requests.get(text)
                if (r.url.find("youtube") != -1):
                    tumcli.create_post({"type":"video","embed":r.url, "caption":stri})
                    return
    tumcli.create_post({"type":"text", "body":stri})

def main():
    while True:
        print("still true!")
        conn = Connection("mongodb://root:u4URSQ0KGiNubhrq1ab4@twumblr-bakanaka-data-0.dotcloud.com:14914")
        coll = conn.db.users
        names = coll.find()
        for sn in names:
            lst = json.loads(requests.get("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + sn["twitter"]).content)
            if "status" in sn:
                matched = False
                consumer = oauth2.Consumer("BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q","p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT")
                token = oauth2.Token(sn["key"],sn["secret"])
                cli = TumblrClient(sn["hostname"],consumer,token)
                for x in range(19, -1, -1):
                    if not matched:
                        print("not matched")
                        if lst[x]["text"] == sn["status"]:
                            print("matched!")
                            matched = True
                    else:
                        print("fuck yeah")
                        tumble(lst[x]["text"], cli)
            sn["status"] = lst[0]["text"]
            coll.save(sn)
        time.sleep(30)

# Bind our callback to the SIGTERM signal and run the daemon:
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
