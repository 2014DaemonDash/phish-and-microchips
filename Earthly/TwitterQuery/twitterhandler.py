# UMCP Daemondash 2014
# Ph!sh&Microchips

# Uses TwitterAPI
# Clone url: https://github.com/geduldig/TwitterAPI.git
from TwitterAPI import TwitterAPI
from TwitterQuery.models import Tweet


# Login Credentials for @PhishNMicrochip <Twitter>
API_key = 'iN7fBBBr7o5UYkLVeatCqVL4A'
API_secret = 'yqCZtmnwkrpb9JOwgH0HLqUNzo1nwYioDLeWpYZHkISXwKNxzg'
access_key = '2807642348-kGRW760kJjAvpUOrVBWvmz8BTXtljVhQdSzyrH2'
access_secret = 'JgVYuEZwvCxFBYNOOwbZSs6RTjHf7L4KWlUqsrPig2Fr2'
api = TwitterAPI(API_key, API_secret, access_key, access_secret)

# Takes list of single quote strings
# and single quote string in format YYYY-MM-DD
def get_tweets(hashtag_list):
    
    tweetls = api.request('statuses/filter', {'track':hashtag_list})
    for tweet in tweetls.get_iterator():
        if(tweet['coordinates'] != None):
            tweetEntry = Tweet(text=tweet['text'], uid=tweet['user']['id'], latitude = tweet['geo']['coordinates'][0], longitude = tweet['geo']['coordinates'][1])
            tweetEntry.save()
    get_tweets(["#love"])
<<<<<<< HEAD

def get_user_friends(uid):
    return api.request('friends/ids', {'q':uid})

=======
    
def get_user_friends(uid):
    return api.request('friends/ids', {'q':uid})


>>>>>>> c295f9cfca3e7ad94965be18adb177bffbfbdb81
