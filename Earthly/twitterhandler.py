# UMCP Daemondash 2014
# Ph!sh&Microchips

# Uses TwitterAPI
# Clone url: https://github.com/geduldig/TwitterAPI.git
from TwitterAPI import TwitterAPI


# Login Credentials for @PhishNMicrochip <Twitter>
API_key = 'iN7fBBBr7o5UYkLVeatCqVL4A'
API_secret = 'yqCZtmnwkrpb9JOwgH0HLqUNzo1nwYioDLeWpYZHkISXwKNxzg'
access_key = '2807642348-kGRW760kJjAvpUOrVBWvmz8BTXtljVhQdSzyrH2'
access_secret = 'JgVYuEZwvCxFBYNOOwbZSs6RTjHf7L4KWlUqsrPig2Fr2'
api = TwitterAPI(API_key, API_secret, access_key, access_secret)


# Takes list of single quote strings
# and single quote string in format YYYY-MM-DD
def get_tweets(hashtag_list, last_time=None):
    for tag in hashtag_list:
        query = tag
        if(last_time !=None):
            query += ' since'
            query += last_time
        tweetls = api.request('search/tweets', {'q':query})#,'g':'39.0012,-76.9317,50mi'})
        for tweet in tweetls.get_iterator():
            if(tweet['coordinates'] !=None):
                print tweet
                print "\n\n\n\n\n"

def get_user_friends(uid):
    return api.request('friends/ids', {'q':uid})

get_tweets(["NashvsHayes"])