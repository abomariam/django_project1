# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150325_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('body', models.CharField(max_length=25)),
                ('reciever', models.ForeignKey(to='user.User', related_name='messages_reciever')),
                ('sender', models.ForeignKey(to='user.User', related_name='messages_sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
