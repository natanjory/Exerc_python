#!/usr/bin/env python
# -*- coding: utf-8 -*- 


def loop_str(string):
    index = -1
    while abs(index) <= len(string):
        letter = string[index]
        print(letter)
        index = index - 1

# for letter in fruit:
#     print(letter)
#    print ('Fazendo um têste')
    
#loop_str('Laranja')    

def loop_for():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print (letter + 'u' + suffix)
        else:
            print(letter + suffix)
            
def count_(word,letter):
    #word = 'banana'
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
            print(count)
    return -1
        
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

string = "PYTHPN IS AWESOME teste t"

print(string.find("P",1))

