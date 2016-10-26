import tweepy


configs = {
    'API KEY': 'FcuBGT2E2vSusk6rNlSfSUQCc',
    'API Secret': 'Lp96ATqrEP4rzoUCiZpBw5b7dXFbJoMCONDFwwuDADjL5S43C2',
    'Access token': '791307771924938752-K1ovtmZGXxasV25GAVsScGu5Mhoc5zF',
    'Access token secret': 'yY2GcZxokNenu88kCQ7F6vVXwhgHipElsXEomQi0TWGwX'
}

auth = tweepy.OAuthHandler(consumer_key=configs['API KEY'],
                           consumer_secret=configs['API Secret'])
auth.set_access_token(configs['Access token'],
                      configs['Access token secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

status = "Hello, World!"
api.update_status(status)
