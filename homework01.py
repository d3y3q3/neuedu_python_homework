#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import time

print('begin')
hPos = 0
tPos = 0

while True:
    paodao = '_' * 70
    n = randint(0,10) + 1
    if n <= 5:
        tPos += 3
    elif 5 < n <= 7:
        tPos -= 6
    else:
        tPos += 1

    if n <= 2:
        hPos = hPos
    elif 3 <= n <= 4:
        hPos += 9
    elif n == 5:
        hPos -= 12
    elif 6 <= n <= 8:
        hPos += 1
    else:
        hPos -= 2

    if tPos >= 70 or hPos >= 70:
        break

    if tPos == hPos:
        paodao = paodao[:tPos] + '咬' + paodao[tPos:]
    else:
        paodao = paodao[:tPos] + '龟' + paodao[tPos:]
        paodao = paodao[:hPos] + '兔' + paodao[hPos:]

    print(paodao)
    time.sleep(0.5)

if tPos > 70:
    print('龟赢')
else:
    print('兔赢')
