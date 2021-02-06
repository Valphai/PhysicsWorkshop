library(reticulate)
use_python("D:/python")
source_python('LatexRead.py')
tab = LatexRead() # tab[["K4"]]

df = data.frame(tab)

U = c(tab[["K0"]], tab[["K2"]], tab[["K4"]])
I = c(tab[["K1"]], tab[["K3"]], tab[["K5"]])
Cewka = c(rep("L1",length(1:10)),rep("L1+L2",length(1:10)),rep("L1+L2+L3",length(1:10)))
dff = data.frame(U,I,Cewka)
dff$I = dff$I*10^-3

niepY = 0.001
niepX = 0.01
xax = "U[V]"
yax = "I[A]"

library(ggplot2)
ggplot(dff, aes(x=U, y=I, color = Cewka)) +
  geom_point(size = 0.2) + 
  xlab(xax) + ylab(yax) +
  geom_smooth(method="lm", se=FALSE) +
  geom_errorbar(data=dff,aes(ymin=I - niepY, ymax= I + niepY),width=.01) +
  geom_errorbarh(data=dff,aes(xmin=U - niepX, xmax=U + niepX))
  
