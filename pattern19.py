# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:05:27 2019

@author: Maharshi
"""

n = int(input("Enter the number of rows : "))

#   1 
#   2    3 
#   4    5    6 
#   7    8    9   10 
#  11   12   13   14   15 

x = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(format(x,">4"),end=' ')
        x += 1
    print()
    
#1    
#2    3    
#4    5    6    
#7    8    9    10   
#11   12   13   14   15  
x = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(format(x,"<4"),end=' ')
        x += 1
    print()