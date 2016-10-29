from twitter import api
import configs

a = api.TwitterBot(configs.config_my)

b = a.tweets_timeline()
c = a.api.followers_ids()

pass