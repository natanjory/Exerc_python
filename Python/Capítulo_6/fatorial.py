# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         for n:1:--
#         n = n*(n-1)
#         n--
        
def factorial(n):
    if n == 0:
        return 1
    else:
        #print("teste")
        recurse = factorial(n-1)
        print(n,"  ",recurse)
        result = n * recurse
        print("teste", result)
        return result
        
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)

n = fibonacci(10)
print("Final ",n)