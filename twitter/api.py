import tweepy
import random
import string


class TwitterBot:
    def __init__(self, credentials):
        auth = tweepy.OAuthHandler(consumer_key=credentials['API KEY'],
                                   consumer_secret=credentials['API Secret'])
        auth.set_access_token(credentials['Access token'],
                              credentials['Access token secret'])
        self.api = tweepy.API(auth)
        
    def update_status(self, status):
        self.api.update_status(status)

    def home_timeline(self,):
        self.api.home_timeline()