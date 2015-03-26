# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replay',
            name='author',
        ),
        migrations.AlterField(
            model_name='replay',
            name='body',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
    ]
