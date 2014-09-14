from django.db import models

class HashTag(models.Model):
    text = models.CharField(max_length = 140, default="")
    score = models.IntegerField(default=0)
    def __str__(self):
        return "{'text':"+self.text+", 'score':"+str(self.score)+"}"

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140, default="0")
    score = models.IntegerField(default=0)
    def __str__(self):
        return "{'name':"+self.name+", 'score':"+str(self.score)+"}"

class Tweet(models.Model):
    text = models.CharField(max_length = 141,default="")
    hashtags = models.CharField(max_length = 141, default="")
    uid = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    datetime = models.DateField(auto_now=True)
    def __str__(self):
        return "{'text':"+self.text+", 'hashtags':"+self.hashtags+", 'uid':"+str(self.uid)+", 'datetime':"+str(self.datetime)+", 'latitude':"+str(self.latitude)+", 'longitude':"+str(self.longitude)+"}"