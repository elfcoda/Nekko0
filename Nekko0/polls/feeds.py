# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.db.models import F
from .models import Article
from .views import SHOW_CONTENT_SPLIT

def delCustomerTag(html):
    html = html.replace('lt_cus', '<')
    html = html.replace('gt_cus', '>')
    return html

class LatestEntriesFeed(Feed):
    title = "某个荒凉的小岛"
    link = "/"
    description = "本死宅被吊打的日常/腾讯称职清洁工/端茶倒水陪笑"

    def items(self):
        return Article.objects.all().order_by(F('created').desc())[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        retHtml = item.content_html
        rssShow = retHtml.split(SHOW_CONTENT_SPLIT)
        if len(rssShow) == 2:
            retHtml = rssShow[0]
        retHtml = delCustomerTag(retHtml)
        return retHtml

    def item_pubdate(self, item):
        return item.created


