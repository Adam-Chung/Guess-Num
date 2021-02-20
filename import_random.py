# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:07:15 2021

@author: fong_
"""
#產生1-100隨機整數
#使用者輸入去猜
#猜對印出恭喜
#猜錯告知大或小
#每次秀出範圍

import random
r = random.randint(1,100)

guess = int(input('guess a number：'))
big_num = 100
sma_num = 1
count = 1

while guess != r:
    
    if guess > r:
        big_num = guess
        print(big_num,'>= guess >=',sma_num,',please try again')
    elif guess < r:
        sma_num = guess
        print(big_num,'>= guess >=',sma_num,',please try again')
    print(count,' guess')
    count =count + 1
    guess = int(input('guess a number：'))  
    
print(count, 'congratulation')