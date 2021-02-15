import LatexRead as lr
from Uncertainty import a,u,ux
from math import pi

kolumny = lr.LatexRead()
U = kolumny["K0"][0:10] 
I1 = [x*1E-3 for x in kolumny["K1"][0:10]]
I2 = [x*1E-3 for x in kolumny["K1"][10:20]]
I3 = [x*1E-3 for x in kolumny["K1"][20:30]]
I4 = [x*1E-3 for x in kolumny["K1"][30:40]]
I5 = [x*1E-3 for x in kolumny["K1"][40:50]]
l = [1.41, 2.37, 3.78, 4.74, 6.15]

def Rho(U,I,l):
    S = pi*((2.5*1E-4)/2)**2
    def R(U,I):
        return 1/a(U,I)
    return (R(U,I)*S)/l

# if __name__ == "__main__":
    # print((Rho(U,I1,l[0])+Rho(U,I2,l[1])+Rho(U,I3,l[2])+Rho(U,I4,l[3])+Rho(U,I5,l[4]))/5)

    # print(ux([Rho(U,I1,l[0]),Rho(U,I2,l[1]),Rho(U,I3,l[2]),Rho(U,I4,l[3]),Rho(U,I5,l[4])]))

    # print(a(U,I1),a(U,I2),a(U,I3),a(U,I4),a(U,I5))
    # print(u(U,I1),u(U,I2),u(U,I3),u(U,I4),u(U,I5))