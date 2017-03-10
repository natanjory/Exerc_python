
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
    
def do_n(s, n):
    print_n(s,n)
    
def recurse():
    recurse()
    
#text = raw_input("Entre com a frase\n") 
#print('Chegou')

#do_n(text, 4)

import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power
ratio2 = signal_power / noise_power
print(ratio)
print(ratio2)
decibels = 10 * math.log10(ratio)
print(decibels)
