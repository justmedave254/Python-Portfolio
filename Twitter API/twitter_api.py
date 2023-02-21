import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authenticate 
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

'''auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)'''

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print(' ')
print(public_tweets[0].text)


user = api.get_user(screen_name='elonmusk')
print(user.screen_name)
print(user.followers_count)
print(' ')
for friend in user.friends():
   print(friend.screen_name)

columns = ['Time', 'User', 'Tweet']
data = []

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)
print(df)

df.to_csv('tweets.csv')
#df.to_excel('tweets.xlsx')
