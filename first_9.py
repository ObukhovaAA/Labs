# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:58:19 2021

@author: Анастасия
"""

def computing():
    
    summ = 0
    sq_sum = 0
    count = 0
    
    while True:
        try:
            num = yield
            summ += num
            sq_sum += num ** 2
            count += 1
            print("Average num", summ / count,
                  "Dispersion", (sq_sum - (summ / count) ** 2),
                  "Num", count)
        except GeneratorExit as exception:
            print("computing stopped")
            raise exception
coroutine = computing()
next(coroutine)

testArr = [2, 4, 5, 7, 1]
for num in testArr:
    coroutine.send(num)
    