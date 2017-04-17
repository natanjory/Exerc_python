#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# eval('1 + 2 * 3')

# eval('math.sqrt(5)')

# eval('type(math.pi)')

def eval_loop():
    while True:
       string = raw_input('Entre com a operação a ser realizada:\n')
       if string == 'done':
           print('ACABOU!!')
           break
       res=eval(string)
       print('O Resultado da operacao e: %f' %res)
    return 
           
        
eval_loop()