import math

def check(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')
 
def write():
    a = input("Entre com o valor de a\n")
    b = input("Entre com o valor de b\n")
    c = input("Entre com o valor de c\n")
    n = input("Entre com o valor de n\n")
    check(int(a),int(b),int(c),int(n))

print('Teste2')
write()



   
