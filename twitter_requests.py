import requests
import tweepy

customer_token = 'FcuBGT2E2vSusk6rNlSfSUQCc'
customer_secret = 'Lp96ATqrEP4rzoUCiZpBw5b7dXFbJoMCONDFwwuDADjL5S43C2'
auth = tweepy.OAuthHandler(customer_token, customer_secret)

auth.set_access_token('791307771924938752-K1ovtmZGXxasV25GAVsScGu5Mhoc5zF', 'yY2GcZxokNenu88kCQ7F6vVXwhgHipElsXEomQi0TWGwX')
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

me = api.me()

tweet = 'Hello, World!'
status = api.update_status(status=tweet)

pass
