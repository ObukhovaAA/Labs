# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:46:45 2021

@author: Анастасия
"""

import re

k = '''def print_gmood(): 
print('   I am happy:)    ')
class Sadspeaker:
def print_bmood(self):
print('   I am sad:(    ')'''

print(re.findall("(?=def).+\s+.+.+", k))

