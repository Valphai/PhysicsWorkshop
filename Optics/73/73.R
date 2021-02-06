library(reticulate)
use_python("C:/Users/Maneq/AppData/Local/Programs/Python/Python37")
source_python('LatexRead.py')
tab = LatexRead() # tab[["K4"]]

df = data.frame(tab)

x = c(tab[["K0"]], tab[["K2"]], tab[["K4"]])
U = c(tab[["K1"]], tab[["K3"]], tab[["K5"]])

x = x[1:(length(x)-1)]
x = x[-c(19)]
U = U[1:(length(U)-1)]
U = U[-c(19)]

dff = data.frame(U,x)
dff <- dff[-c(19), ]
# dff$x = dff$x*10^-2

niepY = 10^-3
niepX = 1 #10^-2
yax = "U[V]"
xax = "x[cm]"

library(ggplot2)
ggplot(dff, aes(x=x, y=U)) +
  geom_point(size = 0.2) + 
  xlab(xax) + ylab(yax) +
  geom_errorbar(data=dff,aes(ymin=U - niepY, ymax= U + niepY),width=.1) +
  geom_errorbarh(data=dff,aes(xmin=x - niepX, xmax=x + niepX))
  
