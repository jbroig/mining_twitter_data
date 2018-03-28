import tweepy
from tweepy import OAuthHandler

import json

consumer_key = "cbFia4ukB6n3daNBIDzpvVlue"
consumer_secret = "rKcF3K54zYByAmC4My1y9k32JfvXLid55THElS3vKf04iGJyFK"
access_token = "940176515966427137-ugNSW3pmH7UFP3K4vIXwwUsmnJq8qK9"
access_secret = "eBfFGZOSBv6Yd0khxgIlOKn0zI5LCyqFRUnHjTzuIVj6P"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Entry point
api = tweepy.API(auth)

# Read timeline
'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    print (status.text)
'''


def process_or_store (tweet):
    print(json.dumps(tweet))

# Process / Store the Json
'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)
'''

#Save last 10 tweets in Json file. 
with open("last_tweets.txt","w") as outfile:

    for status in tweepy.Cursor(api.home_timeline).items(10):
        json.dump(status.text, outfile)