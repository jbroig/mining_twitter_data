#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tweepy
import csv

import credentials

#Autenticación
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        with open('OutputStreaming.csv', 'a') as f:

            writer = csv.writer(f)
            writer.writerow([status.author.screen_name.encode('utf-8'), status.created_at, status.text.encode('utf-8'), status.user.verified, status.lang])

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

#Guardamos los datos en un archivo CSV.
with open('OutputStreaming.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Author', 'Date', 'Text', 'Verified', 'Language'])

streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
#Realizamos un filtro de búsqueda
streamingAPI.filter(track=['Madrid'])
