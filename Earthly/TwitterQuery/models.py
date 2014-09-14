from django.db import models

class HashTag(models.Model):
    text = models.CharField(max_length = 140)
    score = models.IntegerField()

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140)
    score = models.IntegerField()

class Tweet(models.Model):
    text = models.Charfield(max_length = 141)
    uid = models.IntegerField()
    latitude = models.FloatField()
    longitude = model.FloatField()