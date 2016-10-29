<<<<<<< HEAD

from twitter import api
from twitter.configs import my_configs


a = api.TwitterBot(my_configs)
print(a.get_ids())

a.update_status("Hello, world!")

=======
>>>>>>> marina
import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

<<<<<<< HEAD
bot = TwitterBot(settings["my_settings"])
print(bot.tweets_timeline())
=======
bot = TwitterBot(settings)

followers_ids = bot.get_ids_followers()
bot.start_follow_my_followers(followers_ids)
bot.destroy_friendship(followers_ids)
>>>>>>> marina

