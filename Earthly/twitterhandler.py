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
<<<<<<< HEAD
# and single quote string in format YYYY-MM-DD
def get_tweets(hashtag_list, minLat, maxLat, minLon, maxLon, last_time=None):
    for tag in hashtag_list:
        query = tag
        if(last_time !=None):
            query += ' since'
            query += last_time
        tweetls = api.request('statuses/filter', {'track':[query]})
=======
# A single quote string in format '%6.4f,%6.4%,%i%u' [%u is unit i.e. mi]
# A single quote string in format YYYY-MM-DD
def get_tweets(hashtag_list, location=None, last_time=None):
    for tag in hashtag_list:
        query = tag
        if(last_time !=None):
            query = query+' since:'+last_time
        dict = {'q':query}
        if(location !=None):
            dict['g']=location
        print dict
        tweetls = api.request('search/tweets', dict)
>>>>>>> FETCH_HEAD
        for tweet in tweetls.get_iterator():
            if(tweet['coordinates'] != None):
                
                curLat = tweet['geo']['coordinates'][0];
                curLon = tweet['geo']['coordinates'][1];
                
                if(curLat > minLat and curLat < maxLat and curLon > minLon and curLon < maxLon):
                    
                    print tweet['text']
                    print 'Hashtags:'
                    
                    for hashy in tweet['text'].split('#')[1:]:
                        print hashy[:hashy.find(' ')]
                    
                    #print tweet
                    #print tweet['text']
                    #print tweet['geo']['coordinates']

                    print ''

def get_user_friends(uid):
    return api.request('friends/ids', {'q':uid})

<<<<<<< HEAD
get_tweets(["#love"], 37.0012, 40, -73, -76.9317)
=======
print "Running"
get_tweets(["NashvsHayes"],'39.0012,-76.9317,100mi','2013-01-01')
print "Done"
>>>>>>> FETCH_HEAD
