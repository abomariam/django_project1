# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150325_1804'),
        ('thread', '__first__'),
        ('replay', '0002_auto_20150326_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='author',
            field=models.ForeignKey(default=1, to='user.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='replay',
            name='thread',
            field=models.ForeignKey(default=1, to='thread.Thread'),
            preserve_default=False,
        ),
    ]
