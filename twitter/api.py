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

    def tweets_timeline(self, cur_id=None):
        timeline = self.api.user_timeline(id=cur_id)
        return [(tweet.text, tweet.id) for tweet in timeline]

    def get_msg_ids(self, cur_id=None):
        timeline = self.api.user_timeline(id=cur_id)
        return [tweet.id for tweet in timeline]

    def del_msg(self, cur_id):
        self.api.destroy_status(id=cur_id)

    def get_ids_followers(self):
        return self.api.followers_ids()

    def get_ids_friends(self):
        return self.api.friends_ids()

    def start_follow_my_followers(self, id_list):
        for user_id in id_list:
            return self.api.create_friendship(user_id)

    def destroy_friendship(self, id_list):
        for curr_id in id_list:
            return self.api.destroy_friendship(curr_id)
            # self.api.destroy_friendship(curr_id)
