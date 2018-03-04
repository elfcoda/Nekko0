#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端

#一个管道大概会持续30s

#当连接上时，发回去一个connect字符串
def ws_connect(message):
    # print("connect0---------------")
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)
    # print("connect1---------------")

#将发来的信息原样返回
#@channel_session_user_from_http
def ws_message(message):
    # print("message0---------------")
    # message.reply_channel.send({"text": message.content['text']})
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })
    print("---------------")
    print("---------------")
    # print("message1---------------")

#断开连接时发送一个disconnect字符串，当然，他已经收不到了
def ws_disconnect(message):
    # print("dis0---------------")
    # message.reply_channel.send({"close": True})
    Group("chat").discard(message.reply_channel)
    # print("dis1---------------")

