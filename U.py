# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:19:48 2019

@author: Maharshi
"""

import time
letter_height = int(input())
letter_width  = int(input())
pattern = input()
print()

def print_U1(h,w,p):
    for row in range(h):
        for col in range(w):
            if((col==0 or col==w-1) and row!=h-1) or(row==h-1 and 0<col<w-1):
                print(p,end='')
            else:
                print(end=' ')
        print()


if(letter_height>2 and letter_width>2):
    t1 = time.time()
    print_U1(letter_height,letter_width,pattern)
    print()
    print(time.time() - t1)
else:
    print('Letter_height and Letter_width must be grater then 2')