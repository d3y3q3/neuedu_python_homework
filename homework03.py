#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1.定义一个单张扑克类（考虑需要哪些属性），定义一个一副扑克牌类，该类包含一个单张扑克对象的数组（不考虑大小王）。实现一个模拟扑克发牌洗牌的算法；
# 2.电脑随机发出5张牌，判断是以下哪种牌型？（提示，利用Map，List，Set等各种集合的特性可以简化判断）

import random, os, sys


class Card():
    # 单张牌类，包括花色和值
    def __init__(self, color='red', value='1'):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def toString(self):  # 针对AJQK
        strValue = ""
        strTrans = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        if self.value in strTrans:
            strValue = strTrans[self.value]
        else:
            strValue = str(self.value)

        return self.color + strValue


class Poke():
    # 整套牌类
    def __init__(self):
        colors = ('红桃', '黑桃', '方片', '草花')
        values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        self.cards = []
        index = 0
        for i in range(4):
            for j in range(13):
                self.cards.append(Card())
                self.cards[index].setValue(values[j])
                self.cards[index].setColor(colors[i])
                index += 1

    def outputCards(self):
        index2 = 0;
        for i in self.cards:
            if (index2 % 13 == 0):
                print('\n');
            print(i.toString() + " ", end='');
            index2 += 1

    def shuffle(self):  # 洗牌
        random.shuffle(self.cards)

    def getOneHands(self):  # 发5张，这里取洗牌后前五张
        cardHands = []
        for i in range(5):
            cardHands.append(self.cards[i])
        return cardHands

    def judgeHandType(self, hands):  # 判断类型
        bIsSameColor = False
        bIsShunzi = False
        col = []
        val = []
        colset = []
        valset = []
        for i in hands:
            col.append(i.getColor())
            val.append(i.getValue())

        colset = set(col)
        valset = set(val)

        if len(colset) == 1:
            bIsSameColor = True  # 同色
        if (max(valset) - min(valset) == 4) and len(valset) == 5:
            bIsShunzi = True  # 顺子

        if (bIsSameColor and bIsShunzi):
            print('同花顺')
        elif bIsSameColor:
            print('同花')
        elif bIsShunzi:
            print('顺子')
        elif len(valset) == 5:
            print('无对')
        elif len(valset) == 4:
            print('一对')
        else:
            num = []  # 不同值的个数统计集合
            for i in valset:
                num.append(val.count(i))
            if max(num) == 4:
                print('四条')
            elif 1 not in num:
                print('满堂红')
            elif max(num) == 3:
                print('三条')
            else:
                print('两对')

        return


def main(args):
    poke = Poke()
    poke.outputCards()
    poke.shuffle()
    print('\n\n\n洗牌以后')
    poke.outputCards()

    hands = poke.getOneHands()
    print('\n\n\n分到的一手牌是:\n')

    for i in range(5):
        print(hands[i].toString() + "  ", end='')

    print('\n\n\n牌型是:\n')
    poke.judgeHandType(hands)


if __name__ == '__main__':
    main(sys.argv)





