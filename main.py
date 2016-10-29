import json
from twitter.api import TwitterBot


with open('settings.json') as settings_file:
    settings = json.loads(settings_file.read())

bot = TwitterBot(settings["my"])
a = bot.api.followers_ids()[0]
bot.tweets_timeline(cur_id=a)

bot = TwitterBot(settings["my_settings"])
print(bot.tweets_timeline())

msg_id = bot.get_msg_ids()[0]
bot.del_msg(cur_id=msg_id)

