import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings)

followers_ids = bot.get_ids_followers()
bot.start_follow_my_followers(followers_ids)
bot.destroy_friendship(followers_ids)

