import Uncertainty as un
import LatexRead as lr

kolumny = lr.LatexRead(4,4)
R1 = kolumny["K0"] 
R2 = kolumny["K1"]
R3 = kolumny["K2"]
T = kolumny["K3"]

def Eg():
    k = 1.380651 * 1E-23
    a = 3347.546 # Got from calculation in R
    return k * a * 2

print("R1: a: {}, u(x): {},\nR3: a: {}, u(x): {},\nEg: {}".format(un.a(R1,T), un.u(R1,T), 
                                                                    un.a(R3,T), un.u(R3,T),
                                                                    Eg()))