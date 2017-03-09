def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f,val):
    f(val)
    f(val)
    print_twice('spam')
    print_twice('spam')
    
def do_four(f, val):
    do_twice(f,val)
    do_twice(f,val)


do_twice(print_twice, 'spam')
print('')
do_four(print_twice, 'spam')