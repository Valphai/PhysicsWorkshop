from os import path
import re

def LatexRead():
    root = "D:\Zadania\pracownia\PhysicsWorkshop"
    FileName = "dane.txt"
    fil = path.join(root, FileName)

    ileCol = 4 # ile jest kolumn
    wynikCol = 4 # co ile kolejny wynik w kolumnie

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

# print(LatexRead())