from tumblr.oauth import TumblrOAuthClient

consumer_key = 'BmyWZMbAzcK9Y7mEQKTgf1JI4icFlXvfxxkfIzuG9nFFVJfg9Q'
consumer_secret = 'p5ohAI2hT7tSwjVCI0HA8oTpOYAvc3m6tIPAXJGNXkur6PgQdT'

tumblr_oauth = TumblrOAuthClient(consumer_key, consumer_secret)
authorize_url = tumblr_oauth.get_authorize_url()

print "visit: %s" % authorize_url
