from twitter import api
import json
#import configparser

# config = configparser.ConfigParser()
# config.read('settings.json')
# credentials = {}
# for section in config.sections():
#     for key, value in config[section].items():
#         credentials[key] = value

bot = api.TwitterBot(api.configs)
# bot.update_status('Hello, world!')

tl = bot.tweets_timeline()
print(tl)

followers_ids = bot.api.followers_ids()
print(followers_ids)

for follower in followers_ids:
    print(follower.tweets_timeline())