#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

import credentials
import json

#Listener que imprime los tweets 
class StdOutListener(StreamListener):    

    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print("Error code: {0}".format(status))
        #Si el código de error es 420, el stream se desconectará.
        if status == 420:
            
            return False

def main():
    #Autenticación
    l = StdOutListener()
    auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    stream = Stream(auth, l)
    #Filtra los tweets que solo tengan los contenidos que queramos.
    stream.filter(track=['Python'])
        
if __name__ == '__main__':
    main()
    

    
    
