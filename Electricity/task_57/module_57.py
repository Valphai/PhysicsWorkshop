import Uncertainty as un
import LatexRead as lr

kolumny = lr.LatexRead(4,4)
R1 = kolumny["K0"] 
R2 = kolumny["K1"]
R3 = kolumny["K2"]
T = kolumny["K3"]

def Eg():
    k = 8.617 * 1e-5
    a = 3347.546 # Got from calculation in R
    return k * a * 2

# if __name__ == "__main__":
print("R1: a: {}, u(x): {},\nR3: a: {}, u(x): {},\nEg: {}".format(un.a(R1,T),un.u(R1,T), 
                                                            un.a(R3,T),un.u(R3,T),Eg()))
                                                                                        