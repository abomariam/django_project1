# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('password', models.CharField(max_length=200)),
                ('gender', models.CharField(default='m', choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('is_banned', models.BooleanField(verbose_name='Banned', default=False)),
                ('role', models.CharField(default='r', choices=[('r', 'Regular'), ('a', 'Admin')], max_length=1)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('signature', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
