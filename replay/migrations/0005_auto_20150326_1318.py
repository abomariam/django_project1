# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0004_auto_20150326_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replay',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
