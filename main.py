from twitter import api
from twitter.configs import my_configs

a = api.TwitterBot(my_configs)

a.update_status("hello world")

# b = a.tweets_timeline()
# c = a.api.followers_ids()


pass