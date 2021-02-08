library(reticulate)
use_python("D:/python")
source_python('LatexRead.py')
tab = LatexRead() # tab[["K4"]]

df = data.frame(tab)


U = c(tab[["K0"]])
I = c(tab[["K1"]])
Druty = c(rep("L=1.41[m]",length(1:10)),rep("L=2.37[m]",length(1:10)),rep("L=3.78[m]",length(1:10)),
          rep("L=4.74[m]",length(1:10)),rep("L=6.15[m]",length(1:10)))
niepY = c(rep(0.0014,length(1:10)),rep(0.0010,length(1:10)),rep(0.0010,length(1:10)),
          rep(0.00079,length(1:10)),rep(0.00079,length(1:10)))
dff = data.frame(U,I,Druty, niepY)
dff$I = dff$I*10^-3
I = I*10^-3

niepX = 0.079
xax = "U[V]"
yax = "I[A]"

library(ggplot2)
ggplot(dff, aes(x=U, y=I, color = Druty)) +
  geom_point(size = 0.2) + 
  xlab(xax) + ylab(yax) +
  geom_smooth(method="lm", se=FALSE) +
  geom_errorbar(data=dff,aes(ymin=I - niepY, ymax= I + niepY),width=.01) +
  geom_errorbarh(data=dff,aes(xmin=U - niepX, xmax=U + niepX))
  
