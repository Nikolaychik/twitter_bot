
from twitter import api
from twitter.configs import my_configs


a = api.TwitterBot(my_configs)
print(a.get_ids())

a.update_status("Hello, world!")

import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings["my_settings"])
print(bot.tweets_timeline())

