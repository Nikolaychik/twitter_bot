<<<<<<< HEAD
from twitter import api
import configs

a = api.TwitterBot(configs.config_my)

b = a.tweets_timeline()
c = a.api.followers_ids()

pass
=======
import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings)
print(bot.tweets_timeline())
>>>>>>> 61ed4b6e268d69da5d4b8ca5188fd91eee195198
