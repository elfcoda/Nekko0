# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleMsgBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('msg_pickle_str', models.CharField(max_length=100000)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
