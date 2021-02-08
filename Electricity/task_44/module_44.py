from LatexRead import LatexRead
from Uncertainty import a,u
from math import sqrt,pi

kolumny = LatexRead()
U1 = kolumny["K0"] 
I1 = [x*1E-3 for x in kolumny["K1"]]
U2 = kolumny["K2"]
I2 = [x*1E-3 for x in kolumny["K3"]]
U3 = kolumny["K4"]
I3 = [x*1E-3 for x in kolumny["K5"]]

R = [
    36,
    16,
    33
]

def Z(a):
    return 1/a

def L(Z,R):
    omega = 2*pi*50
    return sqrt(Z**2-R**2)/omega

def C(a):
    omega = 2*pi*50
    return a/omega

def uZ(U,I):
    return abs(-1/(a(U,I)**2))*u(U,I)

def uy(U,I,R):
    omega = 2*pi*50
    def uL(U,I,R):
        return Z(a(U,I))/(omega*sqrt(Z(a(U,I))**2-R**2))
    def uC(U,I):
        return -1/(Z(a(U,I))**2*omega)
    
    # return sqrt(uL(U,I,R)**2*uZ(U,I)**2)
    return sqrt(uC(U,I)**2*uZ(U,I)**2)

L1 = L(Z(a(U1,I1)),R[0])
L2 = L(Z(a(U2,I2)),R[0]+R[1]) - L1
L3 = L(Z(a(U3,I3)),R[0]+R[1]+R[2]) - L1 - L2

C1 = C(a(U1,I1))
C2 = 2 * C1
C3 = 4 * C1

# print(L1,L2,L3)
# print(uZ(U1,I1),uZ(U2,I2),uZ(U3,I3))
# print(uy(U1,I1,R[0]),uy(U2,I2,R[0]+R[1]),uy(U3,I3,R[0]+R[1]+R[2]))
# print(C1,C2,C3)