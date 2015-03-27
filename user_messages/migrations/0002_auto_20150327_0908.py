# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 3, 27, 9, 8, 5, 479169, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
