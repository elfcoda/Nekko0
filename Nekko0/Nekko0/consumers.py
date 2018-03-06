#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group, Channel
from channels.sessions import channel_session

#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端

#一个管道大概会持续30s

def ws_disconnect(message):
    message.reply_channel.send({"close": True})
    Group("DM").discard(message.reply_channel)

def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("DM").add(message.reply_channel)

def ws_message(message):
    # message.reply_channel.send({"text": message.content['text']})
    Group("DM").send({
        "text": "[user] %s" % message.content['text'],
    })

def ws_sendDM(dmValue):
    Group("DM").send({
        "text": dmValue,
    })

