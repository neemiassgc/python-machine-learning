from numpy import random as ran
from matplotlib import pyplot as plot

x = ran.uniform(0.0, 5.0, int(1e6))

plot.hist(x, 10)
plot.show()

y = ran.normal(5.0, 1.0, int(1e6))
plot.hist(y, 10)
plot.show()