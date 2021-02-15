import LatexRead as lr
import Operations as op

# 1st series
kolumny = lr.LatexRead(5,5)
Imax = 85.6375
Imin = 0.1
Ial = kolumny["K3"]
uxImax = 0.228924

# 2nd series
# kolumny = lr.LatexRead(2,2)
# t = kolumny["K0"]
# A = kolumny["K1"] # mu A

@op.Beautify
def uF():
    substr = op.SubstractFromList(Imin,Ial)
    div = op.DivideListBy((Imax-Imin)**2, substr)
    return op.FloatTimesList(uxImax, div)

if __name__ == "main":
    # print("u(I_max) = {}".format(un.ux(A)))
    print("u(F) = {}".format(uF()))