import tweepy


class TwitterBot:
    def __init__(self, credentials):
        auth = tweepy.OAuthHandler(consumer_key=credentials['API KEY'],
                                   consumer_secret=credentials['API Secret'])
        auth.set_access_token(credentials['Access token'],
                              credentials['Access token secret'])
        self.api = tweepy.API(auth)
        
    def update_status(self, status):    # обновление статуса
        self.status = status
        self.api.update_status(status)

    def all_tweets(self):   # масив из твитов
        all_tweets = []
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            all_tweets.append(tweet.text)




