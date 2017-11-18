# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171115_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('title_zh', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('content_md', models.TextField()),
                ('content_html', models.TextField()),
                ('tags', models.CharField(max_length=30)),
                ('views', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]
