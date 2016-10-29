from twitter import api
import cinema

bot = api.TwitterBot(api.configs)
# bot.update_status('Hello, world!')

tl = bot.tweets_timeline()
print(tl)

followers_ids = bot.api.followers_ids()
print(followers_ids)

for follower in followers_ids:
    print(follower.tweets_timeline())

c = cinema.MovieCollector()
c.get_actual_movie_list()