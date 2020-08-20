from matplotlib import pyplot as plot
from numpy import random

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# plot.scatter(x, y)
# plot.show()

x = random.normal(5.0, 1.0, int(1e6))
y = random.normal(10.0, 2.0, int(1e6))

plot.scatter(x, y)
plot.show()