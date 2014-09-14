# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterQuery', '0004_tweet_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='datetime',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
