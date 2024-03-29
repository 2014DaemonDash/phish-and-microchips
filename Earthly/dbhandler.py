#
#
from TwitterQuery.models import Tweet, HashTag, TwitterUser


def read_user_score(uid):
    return TwitterUser.objects.get(name=uid).score

def read_tag_score(tag):
    return HashTag.objects.get(text=tag).score

# Adds to user score
def update_user_score(uid, val):
    ch = TwitterUser.objects.get(name=uid)
    ch.score = read_user_score(uid) + val
    ch.save()

# Adds to tag score
def update_tag_score(tag, val):
    ch = HashTag.objects.get(text=tag)
    ch.score = read_user_score(uid) + val
    ch.save()

# Tag in form '#HASHTAG' text__contains=tag,
def query_db(lat_min, lat_max, long_min, long_max, dtstart):
    return Tweet.objects.filter(latitude__gte=lat_min, latitude__lte=lat_max, longitude__gte=long_min, longitude__lte=long_max, datetime__gte=dtstart)


def get_followers(uid):
    return []

def score_update(tweet):
    hashtags = tweet['hashtags']['text']
    total_hashvalue = 0
    for item in hashtags:
        HashTag.objects.get_or_create(text=item)
        total_hashvalue += read_tag_score(item)

    # Update user and follower scores
    update_user_score(tweet['user']['id'])
    TwitterUser.objects.get_or_create(name=tweet['user']['id'])
    for user in get_followers(tweet['user']['id']):
        TwitterUser.objects.get_or_create(name=user['id'])
        update_user_score(user['id'],total_hashvalue/3.3)

    # Update tag scores
    for tag in hashtags:
        update_tag_score(tag,total_hashvalue-read_tag_score(tag))