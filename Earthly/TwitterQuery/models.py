from django.db import models

class HashTag(models.Model):
    text = models.CharField(max_length = 140)
    score = models.IntegerField()
    def __str__(self):
        return "{'text':"+text+", 'score':"+score+"}"

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140)
    score = models.IntegerField()
    def __str__(self):
        return "{'name':"+name+", 'score':"+score+"}"

class Tweet(models.Model):
    text = models.CharField(max_length = 141)
    uid = models.IntegerField()
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return "{'text':"+text+", 'uid':"+uid+", 'datetime':"+datetime+", 'latitude':"+latitude+", 'longitutde':"+longitude+"}"