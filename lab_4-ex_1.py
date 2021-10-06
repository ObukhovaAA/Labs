'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--name", required = True, type = str)
parser.add_argument("--country", required = True, type = str)
parser.add_argument("--petal-colour", required = True, choices = ['R' , 'W' , 'V' , 'B' , 'Y'])
parser.add_argument("--stem-length", required = True, type = int)
parser.add_argument("--with-thorns",  default = False, action = 'store_true')
parser.add_argument("--companion-plants", default = None, nargs = '*')

with open("journal.txt", "a") as output_file:
    args = vars(parser.parse_args())
    json.dump(args, output_file)
    
    