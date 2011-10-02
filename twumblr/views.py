from tumblr.oauth import TumblrOAuthClient
import json
from pymongo import Connection

def gen_url(request):
#    consumer_key = 'BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q'
#    consumer_secret = 'p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT'

#    tumblr_oauth = TumblrOAuthClient(consumer_key, consumer_secret)
#    authorize_url = tumblr_oauth.get_authorize_url()
    return {"url": "fuck"}

def obtain_oauth(request):
#    fp = open("/home/dotcloud/environment.json")
#    dbloc = json.load(fp.read())["DOTCLOUD_DATA_MONGODB_URL"]
#    fp.close()
#    conn = Connection(dbloc)
#    coll = conn.db.users

#    consumer_key = 'BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q'
#    consumer_secret = 'p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT'

#    tumblr_oauth = TumblrOAuthClient(consumer_key, consumer_secret)

    oauth_verifier = request.params["oauth_verifier"]
#    access_token = tumblr_oauth.get_access_token(oauth_verifier)
#    coll.insert({"key" : access_token.key, "secret" : access_token.secret})
#    print "Access key:", access_token.key
#    print "Access Secret:", access_token.secret
    
    return {}
