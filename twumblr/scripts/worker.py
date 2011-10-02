#!/usr/bin/env python

import sys
import time
import signal
from pymongo import Connection

conn = Connection()
coll = conn.db.users()

# Callback called when you run `supervisorctl stop'
def sigterm_handler(signum, frame):
    print >> sys.stderr, "Kaboom Baby!"
    sys.exit(0)

def main():
    while True:
        fp = open("/home/dotcloud/environment.json")
        dbloc = json.load(fp)["DOTCLOUD_DATA_MONGODB_URL"]
        fp.close()
        conn = Connection(dbloc)
        coll = conn.db.users
        names = coll.find():
        for sn in names:
            lst = json.loads(requests.get("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s").content) %sn
            if "status" in sn:
                matched = False
                for x in range(19, -1, -1):
                    if not matched:
                        if lst[x] == sn["status"]:
                            matched = True
                    else:
                        tumble(lst[x]["text"], sn["token"])
            sn["status"] = lst[0]["text"]
        time.sleep(30)

def tumble(stri, token):
    pass

# Bind our callback to the SIGTERM signal and run the daemon:
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
