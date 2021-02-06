from LatexRead import LatexRead
from Niepewnosci import a,u
from statistics import mean

kolumny = LatexRead()
a0 = kolumny["K0"]
a10 = kolumny["K1"]
ax = kolumny["K2"]

print("srednie: a0 {}, a10 {}, ax {}".format(mean(a0),mean(a10),mean(ax)))

def katy():
    def b10():
        return mean(a10) - mean(a0)
    def bx():
        return mean(ax) - mean(a0)
    return "b10 {}, bx {}".format(b10(), bx())