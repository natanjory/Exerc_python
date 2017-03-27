import math

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

def hypotenuse(x,y):
    x2 = x**2
    y2 = y**2
    tmp = x2 + y2
    hyp = math.sqrt(tmp)
    print(hyp)
    
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = math.pi * radius**2
    return a
    
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
    
def is_between(x,y,z):
    if x<=y<=z:
        return True
    else:
        return False

res=is_between(3,6,5)
print(type(res))
print(res)
        
    
#res = circle_area(0,0,3,4)
#print(res)
#print(25*math.pi)

#test = compare(4,5)
#print(test)
        