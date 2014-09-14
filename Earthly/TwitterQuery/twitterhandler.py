# UMCP Daemondash 2014
# Ph!sh&Microchips

# Uses TwitterAPI
# Clone url: https://github.com/geduldig/TwitterAPI.git
from TwitterAPI import TwitterAPI
from TwitterQuery.models import Tweet
import datetime
import sys

# Login Credentials for @PhishNMicrochip <Twitter>
API_key = 'ERiVIhyBcoDFAvCbSlxoUbpHR'
API_secret = '7LQYD68HDEtAJo6WmkoaFaGkM3WGSxmWv5tbE0qQA3kUHL4lFb'
access_key = '2809615567-dMZAOWXtj4x4VqjjqcjgrxXfMoRdUKggcNPtjzs'
access_secret = 'Xs3eBq1c8E7yVm7t7CZ1yoLNOS1mr1Ad8xH9Cjy8IScQU'
api = TwitterAPI(API_key, API_secret, access_key, access_secret)

# Takes list of single quote strings
# and single quote string in format YYYY-MM-DD
def get_tweets(hashtag_list):
    
    tweetls = api.request('statuses/filter', {'track':hashtag_list})
    for tweet in tweetls:

        if(tweet['coordinates'] != None):
            
            print tweet['text']
            
            print unicode(tweet['text']).encode(sys.stdout.encoding, errors='replace')
            
            myHashes = ""
            
            for partialHashtag in tweet['text'].split('#')[1:]:
                myHashes += partialHashtag[:partialHashtag.find(' ')] + ","
            myHashes = myHashes[:len(myHashes) - 1]
            
            tweetEntry = Tweet(text=tweet['text'], hashtags=myHashes, uid=tweet['user']['id'], latitude = tweet['geo']['coordinates'][0], longitude = tweet['geo']['coordinates'][1])
            tweetEntry.save()
