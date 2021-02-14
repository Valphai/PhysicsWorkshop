# You have to set working directory first

library(reticulate)
library(ggplot2)
use_python("C:/Users/Maneq/AppData/Local/Programs/Python/Python37")
source_python('LatexRead.py')
source_python('Uncertainty.py')
tab = LatexRead(5L,5L) # tab[["K4"]] L - declare int

ad = c(tab[["K0"]], tab[["K1"]])
b = c(tab[["K2"]], tab[["K3"]])

M = function(x) b/x
substr = function(x) x - 1
dftemp = data.frame(ad,b)
aTemp = apply(dftemp[1], 2, M)
bTemp = apply(dftemp[2], 2, substr)

dff = data.frame(aTemp,bTemp)

xax = "b [cm]"
yax = "M"

a(bTemp,aTemp)
u(bTemp,aTemp)

ggplot(dff, aes(x=b, y=aTemp)) +
  geom_point(size = 0.2) + 
  xlab(xax) + ylab(yax) +
  geom_smooth(method="lm", se=FALSE)
  # geom_errorbar(data=dff,aes(ymin=aTemp - niepY, ymax= aTemp + niepY)) +
  # geom_errorbarh(data=dff,aes(xmin=b - niepX, xmax=b + niepX))
  
