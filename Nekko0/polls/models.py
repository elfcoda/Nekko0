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
    nickname = models.CharField(max_length=20)
    passwd = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    sex = models.CharField(max_length=2)
    created_date = models.DateTimeField()
    level = models.CharField(max_length=1)
    level_tag = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    introduce = models.CharField(max_length=100)
    avatar_url = models.URLField()

    def __str__(self):
        return self.nickname


