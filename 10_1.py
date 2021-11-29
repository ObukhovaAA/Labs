# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 10:46:58 2021

@author: Анастасия
"""

import argparse 
from multiprocessing import Pool


def prime_factorization(numb):

    numb = int(numb)
    d = 2
    output = [numb]

    while numb != 1:       
        while numb % d == 0:           
            numb //= d            
            output.append(d)
        d += 1
        
    r = str(output[0]) + ":" + str(' '.join(map(str, output[1:])))

    return r


def Parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs = "+")

    return parser


if __name__ == '__main__':
    parser = Parser()
    numbers = parser.parse_args()

    if numbers.input:
        pool = Pool(processes = len(numbers.input))
        r = pool.map(prime_factorization, numbers.input)
        print('\n'.join(map(str, r)))
