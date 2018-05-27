#!/usr/bin/env python
# encoding: utf-8
import math

def isZs2(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def isZs(x):
    if x <= 1:
        return False
    elif x % 2 == 0 and x != 2:
        return False
    elif x % 3 == 0 and x != 3:
        return False
    elif x % 5 == 0 and x != 5:
        return False
    elif x % 7 == 0 and x != 7:
        return False
    else:
        for i in range(3, int(math.sqrt(x))+1, 2):
            if x % i == 0:
                return False
        return True

def getsum(x1):
    sum = 0
    while x1 / 10:
        sum += x1 % 10
        x1 /= 10
    sum += x1
    if isZs(sum):
        return True
    return False

begin = 1000001
count = 0
while True:
    if isZs(begin):
        if getsum(begin):
            count += 1
            print begin
            if count == 2:
                break
    begin += 2


