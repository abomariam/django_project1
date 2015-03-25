# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='lock',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forum',
            name='lock',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
