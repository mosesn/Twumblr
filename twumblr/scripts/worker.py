#!/usr/bin/env python

import sys
import time
import signal
from pymongo import Connection
from tumblr import TumblrClient
import oauth2

conn = Connection()
coll = conn.db.users()

# Callback called when you run `supervisorctl stop'
def sigterm_handler(signum, frame):
    print >> sys.stderr, "Kaboom Baby!"
    sys.exit(0)

def main():
    while True:
        """
        fp = open("/home/dotcloud/environment.json")
        dbloc = json.load(fp)["DOTCLOUD_DATA_MONGODB_URL"]
        fp.close()
        conn = Connection(dbloc)
        coll = conn.db.users
        names = coll.find():
        for sn in names:
            lst = json.loads(requests.get("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + sn["twitter"]).content)
            if "status" in sn:
                matched = False
                consumer = oauth2.Consumer("BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q","p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT")
                token = oauth2.Token(sn["key"],sn["secret"])
                TumblrClient(sn["hostname"],consumer,token)
                for x in range(19, -1, -1):
                    if not matched:
-                        if lst[x] == sn["status"]:
                            matched = True
                    else:
                        tumble(lst[x]["text"], sn["token"])
            sn["status"] = lst[0]["text"]
            coll.save(sn)
            """
        time.sleep(30)

def tumble(stri, tumcli):
    tumcli.create_post({"type":text, "body":stri})

# Bind our callback to the SIGTERM signal and run the daemon:
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
