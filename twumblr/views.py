import json
from pymongo import Connection


def obtain_oauth(request):
    fp = open("/home/dotcloud/environment.json")
    dbloc = json.load(fp.read())["DOTCLOUD_DATA_MONGODB_URL"]
    fp.close()
    conn = Connection(dbloc)
    coll = conn.db.users

    oauth_verifier = request.params["oauth_verifier"]
    access_token = tumblr_oauth.get_access_token(oauth_verifier)
    coll.insert({"key" : access_token.key, "secret" : access_token.secret})
    print "Access key:", access_token.key
    print "Access Secret:", access_token.secret
    
