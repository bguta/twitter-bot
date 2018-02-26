# this is your twitter info
# i removied mine

import tweepy

# your info
consumer_key =
consumer_secret =
access_token =
access_token_secret =


def api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
