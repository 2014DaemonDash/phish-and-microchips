# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterQuery', '0003_auto_20140914_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='hashtags',
            field=models.CharField(default=b'', max_length=141),
            preserve_default=True,
        ),
    ]
