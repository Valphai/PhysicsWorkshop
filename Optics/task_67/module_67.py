import LatexRead as lr
from Uncertainty import ux
from statistics import mean
from math import sqrt

kolumny = lr.LatexRead()
a0 = kolumny["K1"]
a10 = kolumny["K2"]
ax = kolumny["K3"]
c = 0.05

def katy():
    def bx():
        return mean(ax) - mean(a0)
    def b10():
        return mean(a10) - mean(a0)
    def cx():
        return (bx()/b10())*c
    return "b10 {}, bx {}, cx {}".format(b10(), bx(), cx())

print("srednie: a0 {}, a10 {}, ax {},\n{},\nu(a0) {}, u(a10) {}, u(ax) {}".format(
                        mean(a0),mean(a10),mean(ax),katy(),ux(a0),ux(a10),ux(ax)))