def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
    n = len(word)
    num = n/2
    #print(num)
    for x in xrange(num):
        if first(word) == last(word):
            word = middle(word)
            #print(word)
        else:
            return False
    return True
    
bool_ = is_palindrome("NataN")
print(bool_)


# teste = last("Teste")
# print(teste)
# teste2 = middle("ST")
# print(teste2)
