# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0002_auto_20150324_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='lock',
            field=models.CharField(default=False, max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forum',
            name='lock',
            field=models.CharField(default=False, max_length=10),
            preserve_default=True,
        ),
    ]
