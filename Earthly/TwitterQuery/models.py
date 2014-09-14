from django.db import models

class SearchTerm(models.Model):
    text = models.CharField(max_length = 140)
    score = models.IntegerField()

class TwitterUser(models.Model):
    name = models.CharField(max_length = 140)
    score = models.IntegerField()