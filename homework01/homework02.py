#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import random
import time

# 单词库
Words = ['apple', 'pear', 'banana']


# 单词随机选择函数
def getRandomWord():
    global Words
    return Words[random.randint(0, len(Words) - 1)]


# 猜测流程
def getGuess():
    while True:
        guess = input("Guess the Word: ")
        for letter in guess:
            if letter in wrongLetters:
                print("The char: " + letter + " you have already guessed")
                continue

        break
    return guess


# 判别显示流程
def displayGame(secretLetters, wrongLetters, secretWord):
    global guess
    global count
    print("Info: ")
    for letter in guess:
        if letter in secretWord:
            secretLetters += letter
        else:
            wrongLetters += letter

    print("SecretLetters: ", end='')
    for letter in secretLetters:
        print(letter, end=' ')
    print()

    print("WrongLetters: ", end='')
    for letter in wrongLetters:
        print(letter, end=' ')
    print()
    print("Count: " + str(count))
    blanks = '_' * len(secretWord)
    for i in range(len(guess)):
        if i >= len(secretWord):
            break
        if secretWord[i] == guess[i]:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    print("Word: ", end='')
    for i in blanks:
        print(i, end=" ")
    print()
    print()


# 主流程

secretLetters = ''
wrongLetters = ''
secretWord = ''
guess = ""
count = 6

os.system('cls')
secretWord = getRandomWord()
while True:
    displayGame(secretLetters, wrongLetters, secretWord)
    guess = getGuess()
    if guess == secretWord:
        print("You win !")
        break
    else:
        if count <= 0:
            print("You lose !")
            break
        else:
            count -= 1
            continue
