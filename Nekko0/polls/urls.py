#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views
from .feeds import LatestEntriesFeed
from .views import ArticlePublishView, ArticleDetailView, ArticleEditView, \
    RegisterView, LoginView, Logout, MsgBoardListView,  UploadAvatar, \
    UploadUserImage, MsgLike, DeleteMsg, AddOrReplyMsg, newAvatar, \
    NewIndexView, ResumeView, TestView, SendDM, LimeMeOp, CodeListView, \
    CodeDetailView, AnotherWorldView, DonateView, NoneView, LogView, HelloWorldView, FriendsView, \
    ResourceView, UploadImg, UploadImageCanon, HHV

app_name = 'polls'
urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^upload-avatar$', UploadAvatar, name='upload-avatar'),
    url(r'^upload-image$', UploadUserImage, name='upload-image'),
    url(r'^upload-image-canon$', UploadImageCanon, name='upload-image-canon'),
    url(r'^newAvatar$', newAvatar, name='newAvatar'),
    url(r'^upimg$', UploadImg, name='upimg'),

    url(r'^resource$', views.ResourceView.as_view(), name='resource'),    # static/download_resource
    url(r'^rss$', LatestEntriesFeed(), name='rss'),
    url(r'^music$', views.AnotherWorldView.as_view(), name='another_world'),
    url(r'^code/(?P<page>[0-9]+)$', views.CodeListView.as_view(), name='code'),
    url(r'^code/(?P<articleId>[0-9]+)/(?P<page>[0-9]+)$', CodeDetailView.as_view(), name='code_detail'),
    url(r'^test$', views.TestView.as_view(), name='test'),
    url(r'^hhv$', views.HHV.as_view(), name='hhv'),
    url(r'^none$', views.NoneView.as_view(), name='ft-none'),
    url(r'^log$', views.LogView.as_view(), name='log'),
    url(r'^resume$', views.ResumeView.as_view(), name='resume'),
    url(r'^friends$', views.FriendsView.as_view(), name='friends'),

    # url(r'^our_star_and_afar$', views.OurStarAndAfarView.as_view(), name='our_star_and_afar'),
    # url(r'^our_flower_and_light$', views.OurFlowerAndLightView.as_view(), name='our_flower_and_light'),
    # url(r'^our_i_love_you$', views.OurILoveYouView.as_view(), name='our_i_love_you'),

    # url(r'^ourtodo$', views.OurTODOView.as_view(), name='ourtodo'),
    # url(r'^ourstart$', views.OurStartView.as_view(), name='ourstart'),
    url(r'^connect$', views.ConnectView.as_view(), name='connect'),

    # url(r'^ourmemory$', views.OurMemoryView.as_view(), name='ourmemory'),
    # url(r'^ourstory$', views.OurStoryView.as_view(), name='ourstory'),
    # url(r'^ourfuture$', views.OurFutureView.as_view(), name='ourfuture'),
    # url(r'^ourtogether$', views.OurTogetherView.as_view(), name='ourtogether'),
    # url(r'^ourblessing$', views.OurBlessingView.as_view(), name='ourblessing'),
    # url(r'^oureden$', views.OurEdenView.as_view(), name='oureden'),

    url(r'^hi$', views.HelloWorldView.as_view(), name='hw'),
    url(r'^$', views.NewIndexView.as_view(), name='index'),
    url(r'^index$', views.ArticleListView.as_view(), name='blog_index'),
    url(r'^(?P<page>\w+)$', views.ArticleListView.as_view(), name='blog_index_page'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    # url(r'^article/(?P<articleId>\w+\.?\w+)$', ArticleDetailView.as_view(), name='article_detail'),
    # url(r'^article/(?P<articleId>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),

    url(r'^article/(?P<articleId>[0-9]+)/(?P<page>[0-9]+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<articleId>\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),

    # url(r'^DdsafgdadfewaFDsae32DSa3SDA165DS4Fsdada3/$', CommentListView.as_view(), name="article_comment"),
    # 充电
    url(r'^donate/(?P<page>[0-9]+)$', views.DonateView.as_view(), name='donate'),
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

