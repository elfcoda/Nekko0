#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views
from views import ArticlePublishView

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

