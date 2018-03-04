#!/usr/bin/env python
# encoding: utf-8

import os
import channels.asgi

# 这里填的是你的配置文件settings.py的位置
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nekko0.settings")
channel_layer = channels.asgi.get_channel_layer()
