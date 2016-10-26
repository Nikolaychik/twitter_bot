import tweepy


configs = {
    'API KEY': 'TAQvGD5Zpp4CGQPg9mtZfvwEw',
    'API Secret': '5IXo09UE4PwTdWhnawCKFRAY0YaQ002aQEPHbl4EaW5bpeDN9d',
    'Access token': '791307645542162432-lZIf24o0TR1VjA1BSUlWVDP5wDpomLN',
    'Access token secret': 'KqD9KGYxNgS0iYhADrCxbqEC95h6OcPDH6e2u3Tn2uBdm'
}

auth = tweepy.OAuthHandler(consumer_key=configs['API KEY'],
                           consumer_secret=configs['API Secret'])
auth.set_access_token(configs['Access token'],
                      configs['Access token secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
status = "lasldalssssdlasld"
api.update_status(status)
