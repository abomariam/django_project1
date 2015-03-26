# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0010_auto_20150326_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='lock',
        ),
    ]
