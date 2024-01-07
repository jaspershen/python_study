library(tidyverse)
###use ggplot2 to plot the data
mtcars %>% 
ggplot(aes(x = mpg, y = disp)) + 
geom_point(size = 20) +
theme(axis.title = element_text(size = 20),
axis.text = element_text(size = 20)) +
theme_bw()


