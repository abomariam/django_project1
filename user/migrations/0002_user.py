# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('password', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1)),
                ('is_banned', models.BooleanField(default=False, verbose_name='Banned')),
                ('role', models.CharField(choices=[('r', 'Regular'), ('a', 'Admin')], default='r', max_length=1)),
                ('country', django_countries.fields.CountryField(default='EG', max_length=2)),
                ('signature', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
