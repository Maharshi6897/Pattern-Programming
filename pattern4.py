# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:32:30 2019

@author: Maharshi
"""

#       *
#      ***
#     *****
#    *******
#   *********

import time
def pattern4(n,p):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for j in range(2*i+1):
            print(p,end='')
        print()

def pattern4_single(n,p):
    for i in range(n):
        print(' '*(n-i-1)+p*(2*i+1))

lines = int(input("Enter number of rows : "))
p = input("Enter pattern style : ")
print()
t1 = time.time()
pattern4(lines,p)
print(time.time() - t1)
print()
t2 = time.time()
pattern4_single(lines,p)
print(time.time() - t2)