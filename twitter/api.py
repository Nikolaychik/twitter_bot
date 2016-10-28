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
        pass # api.update_status(status)




# configs = {
#     'API KEY': 'FcuBGT2E2vSusk6rNlSfSUQCc',
#     'API Secret': 'Lp96ATqrEP4rzoUCiZpBw5b7dXFbJoMCONDFwwuDADjL5S43C2',
#     'Access token': '791307771924938752-K1ovtmZGXxasV25GAVsScGu5Mhoc5zF',
#     'Access token secret': 'yY2GcZxokNenu88kCQ7F6vVXwhgHipElsXEomQi0TWGwX'
# }
#
# auth = tweepy.OAuthHandler(consumer_key=configs['API KEY'],
#                            consumer_secret=configs['API Secret'])
# auth.set_access_token(configs['Access token'],
#                       configs['Access token secret'])
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# status = "Hello, World!"
#
# for x in range(10):
#   status += random.choice(ascii.letters)
#
# api.update_status(status)