# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:31:39 2021

@author: Анастасия
"""

import threading
import sys
import os

def f1(file, string, num):
    global h 
    h[boo[num]] = [] 
    with open(file, 'r') as book:
        while True:
            line = book.readline()
            if not line:
                break
            if string in line:
                h[boo[num]].append(line)
        sys.stdout.flush()
A = str(sys.argv[1])
Direct = str(sys.argv[2])
boo = os.listdir(Direct)
h = dict()
if __name__ == '__main__':
    
    threads = [
        threading.Thread(target = f1, args = (os.path.join(Direct, boo[i]), A, i))
        for i in range(len(boo))
    ]
    
    for thread in threads:
        thread.start() 
        
    for thread in threads:
        thread.join()  
        
    for head, lines in h.items():
        for line in lines:
            print(f'{head}:', line)
            