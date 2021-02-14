# wykres z 1 tabeli,

import LatexRead as lr
from Uncertainty import a,u
from math import sqrt,pi

kolumny = lr.LatexRead()
x1 = [x*1E-2 for x in kolumny["K0"]]
x2 = [x*1E-2 for x in kolumny["K1"]]

