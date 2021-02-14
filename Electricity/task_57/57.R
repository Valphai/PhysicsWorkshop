library(ggplot2)
library(reticulate)

use_python("C:/Users/Maneq/AppData/Local/Programs/Python/Python37")
source_python('LatexRead.py')
tab = LatexRead(4L,4L) # tab[["K4"]]

df = data.frame(tab)

R13 = c(tab[["K0"]], tab[["K2"]])
t = c(tab[["K3"]], tab[["K3"]])
Oporniki = c(rep("R1",length(1:41)),rep("R3",length(1:41)))
dff = data.frame(R13,t,Oporniki)
# wykres dla R1 i R3
# temperatura to x
R2 = c(tab[["K1"]])
t2 = c(tab[["K3"]])
df2 = data.frame(R2,t2)
df2$t2 = df2$t2+273.15

ln = function(x) log(x)
inv = function(x) 1/x
R2temp = apply(df2[1], 2, ln)
t2temp = apply(df2[2], 2, inv)

df2 = data.frame(R2temp, t2temp)
source_python('Uncertainty.py')
a(t2temp,R2temp)
u(t2temp,R2temp)

niepY = 1
niepX = 1
xax = "T[°C]"
yax = "R[\u03a9]"

ggplot(dff, aes(x=t, y=R13, color = Oporniki)) +
  geom_point(size = 0.2) + 
  xlab(xax) + ylab(yax) +
  geom_smooth(method="lm", se=FALSE) +
  geom_errorbar(data=dff,aes(ymin=R13 - niepY, ymax= R13 + niepY)) +
  geom_errorbarh(data=dff,aes(xmin=t - niepX, xmax=t + niepX))

yax2 = "ln(R)[\u03a9]"
xax2 = "1/T[K^-1]"

ggplot(df2, aes(x=t2temp, y=R2temp)) +
  geom_point(size = 0.2) + 
  xlab(xax2) + ylab(yax2) +
  geom_smooth(method="lm", se=FALSE) 
  # geom_errorbar(data=df2,aes(ymin=R2temp - niepY, ymax= R2temp + niepY)) +
  # geom_errorbarh(data=df2,aes(xmin=t2temp - niepX, xmax=t2temp + niepX))
  
