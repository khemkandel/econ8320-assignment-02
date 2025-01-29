a = 10
b = 15
if a<b:
    print("a is less than b")


a = 10
b = 10
if a==b:
    print("a is equal to b")


True & False
True & True
False | False
False | True


def myfunction( a,b):
    return a*b



myfunction(2,3)
myfunction(2.3,3)
myfunction(2,'bye')



def areaCircle(radius):
    import math
    return math.pi*radius**2

areaCircle(2)


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)  
    
factorial(5)