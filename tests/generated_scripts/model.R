install.packages('tidyverse')
install.packages('lme4')

library(tidyverse)
library(lme4)
# Replace 'PATH' with a path to your data
data <- read.csv('PATH')
glm(formula=Y ~ X2+X1_X_X2+X1, family=gaussian(link='identity'), data=data)
