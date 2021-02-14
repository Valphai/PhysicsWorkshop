# You have to set working directory first

library(reticulate)
library(ggplot2)
use_python("C:/Users/Maneq/AppData/Local/Programs/Python/Python37")
source_python('module_62.py')

kat = c(kolumny[["K0"]])
fAlfa = c(kolumny[["K4"]])

radians = kat*pi/180

dff = data.frame(radians,fAlfa)

t=seq(0,2*pi,2*pi/(length(radians) - 1))

df2 = data.frame(t, cos(t)^2)

xax = "\u03b1"
yax = "Wartosc F(\u03b1)"
niepY = uF()

colors = c("F(a)" = "red", "cos(a)^2" = "blue")

func = ggplot(NULL) +
  geom_point(data = dff, aes(x=radians, y=fAlfa, color = "F(a)"), size = 0.5) +
  geom_errorbar(data=dff,aes(x=radians , ymin=fAlfa - niepY, ymax= fAlfa + niepY,
                             xmin=fAlfa + niepY, xmax=fAlfa + niepY),size = .1) +
  geom_line(data = df2, aes(x=t, y=cos(t)^2, color = "cos(a)^2"), size = 0.2) +
  labs(x = xax,
       y = yax,
       color = "Funkcje") +
  scale_color_manual(values = colors)

func + coord_polar("x")
