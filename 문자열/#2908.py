# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 23:25:04 2022

@author: sunny
"""

a,b=map(int,input().split())
a1=a//100
a2=a%100//10
a3=a%10

b1=b//100
b2=b%100//10
b3=b%10

a=a3*100+a2*10+a1
b=b3*100+b2*10+b1

if(a>b): print(a)
else: print(b)