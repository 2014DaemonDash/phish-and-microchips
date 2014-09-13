from django.db import models

class SearchTerm(models.Model):
    text = models.CharField(max_length = 140)