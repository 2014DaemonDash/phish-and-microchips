from django.db import models

class HashTag(models.Model):
    text = models.CharField(max_length = 140, default="")
    score = models.IntegerField(default=0)

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140, default="0")
    score = models.IntegerField(default=0)

class Tweet(models.Model):
    text = models.CharField(max_length = 141,default="")
    uid = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)