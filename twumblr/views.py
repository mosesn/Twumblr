from tumblr.oauth import TumblrOAuthClient
import json
from pymongo import Connection

consumer_key = 'BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q'
consumer_secret = 'p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT'

tumblr_oauth = TumblrOAuthClient(consumer_key, consumer_secret)

def get_twitter(request):
    return {}

def gen_url(request):
    session = request.session
    authorize_url = tumblr_oauth.get_authorize_url()
    session["secret"] = tumblr_oauth.request_token["oauth_token_secret"]
    session["token"] = tumblr_oauth.request_token["oauth_token"]
    session["twitter"] = request.params["twitter"]
    return {"url":authorize_url} 

def remove_twitter(request):
    fp = open("/home/dotcloud/environment.json")
    dbloc = json.load(fp)["DOTCLOUD_DATA_MONGODB_URL"]
    fp.close()
    conn = Connection(dbloc)
    coll = conn.db.users

    handle = request.params["twitter"]
    coll.remove({"twitter":handle})

def obtain_oauth(request):
    fp = open("/home/dotcloud/environment.json")
    dbloc = json.load(fp)["DOTCLOUD_DATA_MONGODB_URL"]
    fp.close()
    conn = Connection(dbloc)
    coll = conn.db.users

    oauth_verifier = request.params["oauth_verifier"]

    session = request.session
    tumblr_oauth.request_token = {"oauth_token_secret":session["secret"],"oauth_token":session["token"]}
    access_token = tumblr_oauth.get_access_token(oauth_verifier)

    access_key = access_token.key
    access_secret = access_token.secret

#    r = requests.post("api.tumblr.com/v2/user/info", params={"api_key":access_key})
    return {"data":""}
#    return {"data":r.content}

#    coll.insert({"key" : access_token.key, "secret" : access_token.secret, "twitter":session["twitter"]})
#    return coll.find_one( {"key" : access_token.key, "secret" : access_token.secret})
#    print "Access key:", access_token.key
#    print "Access Secret:", access_token.secret
    
#    return {}
