#!/usr/bin/env python
# -*- coding: utf-8 -*- 

transp1 = 3
transp2 = 0.75

livro = input('Entre com o preço do livro: ')
ncopias = input('Insira o número de cópias desejadas ')

print(type(livro))

desconto = (float(livro) / 100.0 * 40)
#print(desconto)

custo = ((float(livro) - desconto)*float(ncopias)) + transp1 + ((float(ncopias)-1)*transp2)

#custo = (float(livro)-float(desconto))+float(transp1)+((float(ncopias)-1)*float(transp2))
print("O valor final da venda é R$",custo)