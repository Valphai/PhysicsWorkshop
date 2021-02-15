import Uncertainty as un
import Operations as op
import LatexRead as lr
from statistics import mean


# 1st series
# kolumny = lr.LatexRead(5,5)
# apom = kolumny["K0"] 
# apow = kolumny["K1"]
# bpom = kolumny["K2"] 
# bpow = kolumny["K3"]
# l = kolumny["K4"]

# 2nd and 3rd series
kolumny = lr.LatexRead(3,3)
apow = kolumny["K0"] 
bpom = kolumny["K1"]
l = kolumny["K2"]

def bd(x,y): # for b and d
    return op.substract(x,y)

@op.Beautify
def f(x,y):
    return [(a*b)/(a+b) for a, b in zip(x, y)]

@op.Beautify
def fui(x,y):
    dividedNums = op.divide(op.PowerList(2, bd(x,y)),l)
    return op.FloatTimesList((1/4), op.substract(l, dividedNums))

# if __name__ == "__main__":

    # print("d = {}".format(bd(bpom, apow)))

    # print("pom: f = {}".format(f(apom, bpom)))
    # print("pow: f = {}".format(f(apow, bpow)))
    # print("f_sr = {}".format(mean(f(apom, bpom) + f(apow, bpow))))
    # print("u(f) = {}".format(un.ux(f(apom, bpom) + f(apow, bpow))))

    # print("f2 = {}\nf_s2 = {}\n u2(f) = {}".format(fui(apow[:9],bpom[:9]), mean(fui(apow[:9],bpom[:9])),
    #                                                                     un.ux(fui(apow[:9],bpom[:9]))))
    # print("f3 = {}\nf_s3 = {}\n u3(f) = {}".format(fui(apow[9:],bpom[9:]), mean(fui(apow[9:],bpom[9:])),
    #                                                                     un.ux(fui(apow[9:],bpom[9:]))))

