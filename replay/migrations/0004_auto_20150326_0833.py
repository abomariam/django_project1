# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0003_auto_20150326_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replay',
            name='title',
        ),
        migrations.AlterField(
            model_name='replay',
            name='body',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
