# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_forum', '0004_auto_20150324_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='lock',
        ),
    ]
