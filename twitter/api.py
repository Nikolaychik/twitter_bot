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

    def tweets_timeline(self, cur_id=None):
        timeline = self.api.user_timeline(id=cur_id)
        return [(tweet.text, tweet.id) for tweet in timeline]

    def get_msg_ids(self, cur_id=None):
        timeline = self.api.user_timeline(id=cur_id)
        return [tweet.id for tweet in timeline]

    def del_msg(self, cur_id):
        self.api.destroy_status(id=cur_id)


# Test comment

