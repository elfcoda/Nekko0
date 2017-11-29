#!/usr/bin/env python
# encoding: utf-8

import pickle

msg = []
m1 = [101, "1@q.com", "2017-5-21", "hello world", 23, ""]
m2 = [102, "2@q.com", "2017-7-21", "hello world222", 25, "101name"]


msg.append(m1)
msg.append(m2)

str_msg = pickle.dumps(msg)
print str_msg

print "---------------------"
list_msg = pickle.loads(str_msg)
for dic_msg in list_msg:
    print dic_msg[4]
