#
#
import TwitterQuery.models


# Pulls user score
def read_user_score(uid):
    print ""

# Pulls tag score
def read_tag_score(tag):
    print ""

# Adds to user score
def update_user_score(uid, val):
    print ""

# Adds to tag score
def update_tag_score(tag, val):
    print ""

def get_followers(uid):
    print ""

def score_update(tweet):
    hashtags = tweet['hashtags']['text']
    total_hashvalue = 0
    for item in hashtags:
        total_hashvalue += read_tag_score(item)

    # Update user and follower scores
    for contributor in tweet['contributors']:
        update_user_score(contributor['id'], total_hashvalue)
    update_user_score(tweet['user']['id'])
    for user in get_followers(tweet['user']['id']):
        update_user_score(user['id'],total_hashvalue/3.3)

    # Update tag scores
    for tag in hashtags:
        update_tag_score(tag,total_hashvalue-read_tag_score(tag))