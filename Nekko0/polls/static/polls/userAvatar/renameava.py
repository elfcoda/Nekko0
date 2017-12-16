#!/usr/bin/env python
# encoding: utf-8

import os

fl = os.listdir("./")
i = 1
for f in fl:
    if f != "renameava.py":
        new_name = "github" + str(i) + ".png"
        os.rename(f, new_name)
        i += 1

