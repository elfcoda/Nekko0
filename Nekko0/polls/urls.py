#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views
from .views import ArticlePublishView, ArticleDetailView, ArticleEditView, \
    RegisterView, LoginView, Logout, MsgBoardListView,  UploadAvatar, \
    UploadUserImage, MsgLike, DeleteMsg, AddOrReplyMsg, newAvatar, \
    NewIndexView, ResumeView, TestView, SendDM, LimeMeOp

app_name = 'polls'
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^upload-avatar$', UploadAvatar, name='upload-avatar'),
    url(r'^upload-image$', UploadUserImage, name='upload-image'),
    url(r'^newAvatar$', newAvatar, name='newAvatar'),


    url(r'^test$', views.TestView.as_view(), name='test'),
    url(r'^resume$', views.ResumeView.as_view(), name='resume'),
    url(r'^$', views.NewIndexView.as_view(), name='index'),
    url(r'^index$', views.ArticleListView.as_view(), name='blog_index'),
    url(r'^(?P<page>\w+)$', views.ArticleListView.as_view(), name='blog_index_page'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    # url(r'^article/(?P<articleId>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    # url(r'^article/(?P<articleId>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),

    url(r'^article/(?P<articleId>[0-9]+)/(?P<page>[0-9]+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<articleId>\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),

    # url(r'^DdsafgdadfewaFDsae32DSa3SDA165DS4Fsdada3/$', CommentListView.as_view(), name="article_comment"),
    # 留言板
    url(r'^msgboard/(?P<articleId>[0-9]+)/(?P<page>[0-9]+)$', MsgBoardListView.as_view(), name='msgboard'),
    url(r'^Gfdre8Dfd4s37d48sas3dD42D94f328GA7s4At23/$', MsgLike, name='msglike'),
    url(r'^Gfdre8Fgt4s37d48sas3dD42D944dfffTysy6Ks3/$', SendDM, name='sendDM'),
    url(r'^GfdfdG6y7ds37d48sRft67H3D9434F56g5sy6Ks3/$', LimeMeOp, name='likemeOP'),
    url(r'^Gfdre8Dfd44Y7d48sas3dD4F8S4f328GA77Yot25/$', DeleteMsg, name='deleteMsg'),
    url(r'^GfdrE8Dfr44Y7d48sas3RgYF8S4f328G46G7St25/$', AddOrReplyMsg, name='msgAddOrReply'),
    # url(r'^msgboard/(?P<articleId>[0-9]+)/(?P<page>[0-9]+)$', MsgBoardListView.as_view(), name='msgboard'),

    # url(r'^)

    # url(r'^$', views.IndexView.as_view(), name='index'),之前练习用的
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

