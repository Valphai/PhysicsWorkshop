import os
import re

def LatexRead(ileCol, wynikCol):# (ile jest kolumn, co ile kolejny wynik w kolumnie)
    root = os.getcwd()
    FileName = "dane.txt"
    fil = os.path.join(root, FileName)

    kolumny = {"K{}".format(i) : [] for i in range(ileCol)}

    with open(fil, "r+") as f:
        def Przecinki():
            return f.read().replace(",",".")
        data = re.findall(r"[-+]?\d*\.\d+|\d+", Przecinki()) # f.read()
        
        def DivideByColumn():
            nonlocal data
            for i in kolumny:
                for j in range(len(data)):
                    if j % wynikCol == 0:
                        kolumny[i].append(float(data[j]))
                data = data[1:]
            return kolumny

    return DivideByColumn()