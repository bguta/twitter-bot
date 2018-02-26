# this is your twitter info
# i removied mine but you can add yours and it will do the exact same thing

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
