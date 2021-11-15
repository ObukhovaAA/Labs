'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def author(_author):
    def inner(f):
        f.author = _author
        return f
    return inner

@author("ivanov ivan ivanovich")
def add2(num: int) -> int:
    return num + 2

print(add2.author)

