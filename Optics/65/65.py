from statistics import mean
from LatexRead import LatexRead
import Uncertainty as niep

kolumny = LatexRead()
x1 = [x*1E-3 for x in kolumny["K0"]]
x2 = [x*1E-3 for x in kolumny["K1"]]
dx = [x*1E-3 for x in kolumny["K2"]]
y1 = [x*1E-3 for x in kolumny["K3"]]
y2 = [x*1E-3 for x in kolumny["K4"]]
dy = [x*1E-3 for x in kolumny["K5"]]

def OneToNList(n):
    return [i for i in range(1,n+1)]

def Srednie(x,y):
    return niep.CutAfterDot([(i+j)/2 for i, j in zip(x,y)])

def Promienie(x,y):
    return niep.CutAfterDot([i/2 for i in Srednie(x,y)])

def R(r):
    lamb = 589 * 1E-9
    squared_numbers = list(map(niep.square, r))
    multip_numbers = niep.FloatTimesList(lamb,OneToNList(len(r)))
    return niep.CutAfterDot(niep.divide(squared_numbers,multip_numbers))

bezDwoch =  [i for i in R(Promienie(dx,dy)) if i not in (4.13347, 4.151725)] # 6 i 8 prazek

print("{}\n{}\n{}\n{}\n{}".format(Srednie(dx,dy), Promienie(dx,dy),bezDwoch,
                                  mean(bezDwoch),niep.ux(bezDwoch)))