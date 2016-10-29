import tweepy


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
        return [[tweet.text, tweet.id] for tweet in timeline]

    def get_ids(self):
        return self.api.followers_ids()

# Test comment
