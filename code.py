import tweepy
from textblob import TextBlob
import csv
import numpy as np
import pandas as pd
import re

# Step 1 - Authenticate
consumer_key= 'AJWi3wugnQIMXqns9ll5Wzp06'
consumer_secret= 'DNj7mtG1yqm1DCSyWr3A6dRpNkuZWj5WDVZv3YjNVvry6kVIco'

access_token='4766875772-7N81v8LFmCsP6kqRY3cJJI7kBdmXpwcfs25sdPt'
access_token_secret='n2f2VaprmN0iDVJslYu4tTbLDyKKaPa4SarpnOMYIMZoI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search= input('Enter keyword to search')
noofterms = input('enter number of results you want')
tweets =api.search(search, count = noofterms)

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_label(analysis, threshold = 0):
    if analysis.sentiment[0] > threshold:
        return 'positive'
    elif analysis.sentiment[0] == threshold:
        return 'neutral'
    else:
        return 'negative'

df =[]

for tweet in tweets:
    #print (tweet.text)
    c_tweet=clean_tweet(tweet.text)
    analysis = TextBlob(c_tweet)
    label= get_label(analysis)
    #print(label)
    df.append({'Tweet': c_tweet , 'Sentiment':label  })

df=pd.DataFrame(df)
df.head()

df.to_csv('data.csv', sep=',')
