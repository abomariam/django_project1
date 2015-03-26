# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0009_auto_20150325_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='forum',
            unique_together=set([('name', 'category')]),
        ),
    ]
