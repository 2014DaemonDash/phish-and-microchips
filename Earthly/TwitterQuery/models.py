from django.db import models
import datetime as dt

class HashTag(models.Model):
    text = models.CharField(max_length = 140, default="")
    score = models.IntegerField(default=0)
    def as_dict(self):
        return {'text':self.text, 'score':str(self.score)}

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140, default="0")
    score = models.IntegerField(default=0)
    def as_dict(self):
        return {'name':self.name, 'score':str(self.score)}

class Tweet(models.Model):
    text = models.CharField(max_length = 141,default="")
    hashtags = models.CharField(max_length = 141, default="")
    uid = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    datetime = models.DateTimeField(default=dt.datetime.now)
    def as_dict(self):
        return {'text':self.text,
                'hashtags':self.hashtags,
                'uid':str(self.uid),
                'datetime':str(self.datetime),
                'latitude':str(self.latitude),
                'longitude':str(self.longitude),
                }