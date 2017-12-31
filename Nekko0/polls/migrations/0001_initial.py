# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=201)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='SingleMsgBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('msg_pickle_str', models.TextField(max_length=100000)),
                ('is_exist', models.IntegerField()),
                ('hash_value', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=2)),
                ('created_date', models.DateTimeField()),
                ('com_power', models.IntegerField(default=0)),
                ('level_tag', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField()),
                ('introduce', models.CharField(max_length=100)),
                ('avatar_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
