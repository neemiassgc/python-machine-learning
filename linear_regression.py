from matplotlib import pyplot as plot
from scipy import stats
from data import x, y

slope, intercept, r, p, std_err = stats.linregress(x, y)

def fun(g):
	return slope * g + intercept

my_model = list(map(fun, x))

# print(r)

# plot.scatter(x, y)
# plot.plot(x, my_model)
# plot.show()

print(fun(10))