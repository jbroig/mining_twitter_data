#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import credentials
import json
import pandas as pd
import datetime
import unicodedata

#Auth
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

def createDataFrame():

    columns = ["Date",'Tweet',"User","Verified","Retweet_count","Favorite_count"]
    #Note: we could create an empty DataFrame (with NaNs) simply by writing:

    df = pd.DataFrame(columns=columns)
    df = df.fillna(0)
    return df

def saveInDf():

    df = createDataFrame()

    for tweet in tweepy.Cursor(api.home_timeline).items(10):   

        # print tweet
        json_str = tweet._json
        # print json_str
        print "--------------------------------"
        # print type(tweet)

        tweet_str = tweet.text
        tweet_str = unicodedata.normalize('NFKD',tweet_str).encode('ascii','ignore')     

        user = json_str["user"]["name"]
        verified = json_str["user"]["verified"]
        retweet_count = json_str["retweet_count"]
        favorite_count = json_str["favorite_count"]

        df = df.append({"Tweet":str(tweet_str), "User":str(user), "Verified":str(verified), "Retweet_count":str(retweet_count), "Favorite_count":str(favorite_count)},ignore_index= True)

    return df

def dfToCsv():
    df = saveInDf()
    df.to_csv("test.csv")


if __name__ == "__main__":
    saveInDf()
    dfToCsv()
    