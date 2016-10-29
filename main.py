import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings)
print(bot.tweets_timeline())
