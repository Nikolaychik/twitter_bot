<<<<<<< HEAD
from twitter import api
from twitter.configs import my_configs


a = api.TwitterBot(my_configs)
print(a.get_ids())

a.update_status("Hello, world!")a
=======
import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings)
print(bot.tweets_timeline())
>>>>>>> c43a8dd87f2b166ed66079dbde70fb9cf288b8e9
