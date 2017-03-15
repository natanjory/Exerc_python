import math


def verif_triangle(a,b,c):
    if a + b < c:
        print ('No')
    elif a + c < b:
        print ('No')
    elif b + c < a:
        print ('No')
    else:
        print ('Yes')
        
def input_triangle():
    a = input('Informe o tamanho do 1º graveto:\n')
    b = input('Informe o tamanho do 2º graveto:\n')
    c = input('Informe o tamanho do 3º graveto:\n')
    verif_triangle(int(a),int(b),int(c))
    
input_triangle()
        
    
        
    

