# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0008_auto_20150324_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
    ]
