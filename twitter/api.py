import tweepy
import json

with open('settings.json') as config_file:
    configs = json.load(config_file)


class TwitterBot:
    def __init__(self, credentials):
        auth = tweepy.OAuthHandler(consumer_key=credentials['API KEY'],
                                   consumer_secret=credentials['API Secret'])
        auth.set_access_token(credentials['Access token'],
                              credentials['Access token secret'])
        self.api = tweepy.API(auth)

    def update_status(self, status):
        self.api.update_status(status)

    def tweets_timeline(self):
        timeline = self.api.user_timeline()
        return [(tweet.id, tweet.text) for tweet in timeline]