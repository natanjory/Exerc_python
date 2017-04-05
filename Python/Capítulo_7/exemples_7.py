#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import math

def tabuada_9(n):
    if n<=0 or n>9:
        print('Não rola!!!')
        return
    else:
        pri = n-1
        seg = 10-n
        val=str(pri)+str(seg)
        val2=float(val)
        print(val2)
        return
        

def mysqrt(a):
    x=50
    while True:
     #print(x)
     y = (float(x) + float(a)/x) / 2
     if abs(y-x) < 0.000000002 :
         return y
     x=y
     
# y = test_square_root(25)
# print(y)
def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    for x in range(0, 10):
        y = mysqrt(x)-math.sqrt(x)
        print(x,'%.5f' %mysqrt(x),"   "'%.3f' %math.sqrt(x),y)
    return

test_square_root()
    
#,mysqrt(x),math.sqrt(x),mysqrt(x)-sqrt(x)