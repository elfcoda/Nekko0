#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views
from views import ArticlePublishView, ArticleDetailView, ArticleEditView, \
    RegisterView, LoginView, Logout, MsgBoardListView, MsgBoardFormView

app_name = 'polls'
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', Logout, name='logout'),

    url(r'^$', views.ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),

    # 留言板
    url(r'^msgboard/(?P<page>[0-9]+)$', MsgBoardListView.as_view(), name='msgboard'),

    # url(r'^)

    # url(r'^$', views.IndexView.as_view(), name='index'),之前练习用的
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

