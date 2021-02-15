########################## operatrions on list elements
def multiply(x,y):
    return [a*b for a, b in zip(x, y)]

def divide(x,y):
    return [a/b for a, b in zip(x, y)]

def substract(li1, li2):
    return [a-b for a, b in zip(li1,li2)]
########################## Decorator cuts decimal points to nth place
def Beautify(item, decimalPoints=6): 
    def solution(*args):
        return eval("%.{}f".format(decimalPoints) % item(*args))

    def listSolution(*args):
        return [float(i) for i in ["%.{}f".format(decimalPoints) % i for i in item(*args)]]
    
    def decide(*args):
        if isinstance(item(*args), float):
            return solution(*args)
        else:
            return listSolution(*args)
    return decide
########################## TypeError: can't multiply sequence by non-int of type 'float'
def PowerList(fl,li):
    return [x**fl for x in li]

def FloatTimesList(fl,li):
    return [x*fl for x in li]

def AddFloatToList(fl,li):
    return [x+fl for x in li]

def SubstractFromList(fl,li):
    return [x-fl for x in li]

def DivideListBy(fl,li):
    return [x/fl for x in li]
########################## 