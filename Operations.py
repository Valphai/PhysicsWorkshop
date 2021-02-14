########################## operatrions on list elements
def multiply(x,y):
    return [a*b for a, b in zip(x, y)]

def divide(x,y):
    return [a/b for a, b in zip(x, y)]

def substract(li1, li2):
    return [a-b for a, b in zip(li1,li2)]

def BeautifyList(item): # For list of solutions
    def solutions(*args):
        return [float(i) for i in ["%.6f" % i for i in item(*args)]]
    return solutions
##########################  For one solution
def Beautify(item): 
    def solution(*args):
        return eval("%.6f" % item(*args))
    return solution
########################## TypeError: can't multiply sequence by non-int of type 'float'
def FloatTimesList(fl,li):
    return [x*fl for x in li]

def PowerList(fl,li):
    return [x**fl for x in li]

def AddFloatToList(fl,li):
    return [x+fl for x in li]

def SubstractFromList(fl,li):
    return [x-fl for x in li]
########################## 