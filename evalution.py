import numpy
from matplotlib import pyplot as plot
from sklearn.metrics import r2_score

# training & testing

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# plot.scatter(x, y)
# plot.show()

train_x, train_y = x[:80], y[:80]
test_x, test_y = x[80:], y[80:]


mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

# myline = numpy.linspace(0, 6, 100)
# plot.scatter(train_x, train_y)
# plot.plot(myline, mymodel(myline))
# plot.show() 

print(mymodel(5.5))