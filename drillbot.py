# Import the required module for text
# to speech conversion
from gtts import gTTS
import random
import tweepy
import json

data = {}

with open('twittercred.json') as json_file:
   data = json.load(json_file)

consumer_key = data['consumer_key']
consumer_secret = data['consumer_secret']
access_token = data['access_token']
access_token_secret = data['access_token_secret']

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

name = 'dril'
tweetCount = 10
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.text)

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
tweet = random.choice(results)
mytext = tweet.text

# Language in which you want to convert
language = 'en-uk'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("drilbot.mp3")

# Playing the converted file
os.system("start drilbot.mp3")