# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=201)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


@python_2_unicode_compatible
class Article(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=50)
    title_zh = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content_md = models.TextField()
    content_html = models.TextField()
    tags = models.CharField(max_length=30)
    views = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.title_zh


@python_2_unicode_compatible
class Userinfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    sex = models.CharField(max_length=2)
    created_date = models.DateTimeField()
    com_power = models.IntegerField(default=0)
    # 算力值决定level，所以去掉level字段
    # level = models.CharField(max_length=1)
    level_tag = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    introduce = models.CharField(max_length=100)
    avatar_url = models.URLField()

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class SingleMsgBoard(models.Model):
    article_id = models.IntegerField()
    msg_pickle_str = models.TextField(max_length=100000)
    is_exist = models.IntegerField()                # 通过这个在数据库进行筛选，得到所有未删除的评论
    hash_value = models.CharField(max_length=15)    # 存进数据库时指定一个哈希值，可以用哈希值取出数据，得到id

    # msger_id = models.IntegerField()
    # msger_email = models.CharField(max_length=50)
    # msger_pub_date = models.DateTimeField()
    # msger_pub_content = models.CharField(max_length=1000)
    # msger_liked = models.IntegerField()
    # reply_to_username = models.CharField(max_length=20)

    def __str__(self):
        return self.article_id




