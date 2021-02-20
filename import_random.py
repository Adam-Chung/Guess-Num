# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:43:29 2021

@author: fong_
"""
#產生1-100隨機整數
#使用者輸入去猜
#猜對印出恭喜
#猜錯告知大或小

import random
r = random.randint(1,100)

guess = int(input('guess a number：'))
while guess != r:
    if guess > r:
        print('<guess, please try again')
        guess = int(input('guess a number：'))
    elif guess < r:
        print('>guess, please try again')
        guess = int(input('guess a number：'))

print('congratulation')
    