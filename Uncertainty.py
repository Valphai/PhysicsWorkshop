import Operations as op
from math import sqrt
from statistics import mean

# Always remember to convert units

# PROSTA REGRESJI
##########################
def D(x):
    n = len(x)
    squared_numbers = op.PowerList(2, x)
    return n*sum(squared_numbers)-sum(x)**2

@op.Beautify
def a(x,y):
    n = len(x)
    return (n*sum(op.multiply(x,y))-(sum(x)*(sum(y))))/D(x)

@op.Beautify
def u(x,y): # u(a)
    n = len(x)

    def b(x,y):
        squared_numbers = op.PowerList(2, x)
        return ((sum(squared_numbers)*sum(y))-(sum(x)*sum(op.multiply(x,y))))/D(x)

    def sy(x,y):
        addThis = op.AddFloatToList(b(x,y),op.FloatTimesList(a(x,y), x))
        squared_numbers = op.PowerList(2, op.substract(y,addThis))
        return sqrt((sum(squared_numbers)/(n-2)))

    return sy(x,y)*sqrt(n/D(x))

########################## wzor (2) == (17)
def ux(x):
    n = len(x)
    diff = op.SubstractFromList(mean(x),x)
    squared_numbers = op.PowerList(2, diff)
    return sqrt((1/(n*(n-1)))*sum(squared_numbers))
########################## 