from LatexRead import LatexRead
from math import sqrt
from statistics import mean

########################## operatrions on list elements
def square(number):
    return number ** 2

def multiply(x,y):
    return [a*b for a, b in zip(x, y)]

def divide(x,y):
    return [a/b for a, b in zip(x, y)]

def substract(li1, li2):
    return [i-j for i, j in zip(li1,li2)]

def CutAfterDot(x):
    return [float(i) for i in ["%.6f" % i for i in x]]
########################## TypeError: can't multiply sequence by non-int of type 'float'
def FloatTimesList(fl,li):
    return [x*fl for x in li]

def AddFloatToList(fl,li):
    return [x+fl for x in li]

def SubstractFromList(fl,li):
    return [x-fl for x in li]
########################## 

# PROSTA REGRESJI
##########################
def D(x):
    n = len(x)
    squared_numbers = list(map(square, x))
    return n*sum(squared_numbers)-sum(x)**2

def a(x,y): # poprawic jednostki!!!
    n = len(x)
    return (n*sum(multiply(x,y))-(sum(x)*(sum(y))))/D(x)

def u(x,y): # u(a)
    n = len(x)

    def b(x,y):
        squared_numbers = list(map(square, x))
        return ((sum(squared_numbers)*sum(y))-(sum(x)*sum(multiply(x,y))))/D(x)

    def sy(x,y):
        addThis = AddFloatToList(b(x,y),FloatTimesList(a(x,y), x))
        squared_numbers = list(map(square, substract(y,addThis)))
        return sqrt((sum(squared_numbers)/(n-2)))

    return sy(x,y)*sqrt(n/D(x))

########################## wzor (2)
def ux(x):
    n = len(x)
    diff = SubstractFromList(mean(x),x)
    squared_numbers = list(map(square, diff))
    return sqrt((1/(n*(n-1)))*sum(squared_numbers))
##########################