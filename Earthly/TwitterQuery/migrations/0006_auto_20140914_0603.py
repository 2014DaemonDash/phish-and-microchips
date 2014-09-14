# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterQuery', '0005_auto_20140914_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
