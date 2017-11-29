#!/usr/bin/env python
# encoding: utf-8

import pickle
import datetime

msg = []
m1 = {
    "submsger_id": 101,
    "submsger_email": "1@q.com",
    "submsger_pub_date": "2017-10-21",
    "submsger_pub_content": "hello world",
    "submsger_liked": 23,
    "reply_to_username": ""
}

m2 = {
    "submsger_id": 102,
    "submsger_email": "2@q.com",
    "submsger_pub_date": "2017-10-31",
    "submsger_pub_content": "hello world22222",
    "submsger_liked": 22,
    "reply_to_username": "yy"
}

msg.append(m1)
msg.append(m2)

str_msg = pickle.dumps(msg)
print str_msg.__len__()

print "---------------------"
list_msg = pickle.loads(str_msg)
for dic_msg in list_msg:
    print dic_msg['submsger_liked']
