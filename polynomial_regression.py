from matplotlib import pyplot as plot
from numpy import poly1d, linspace, polyfit
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

my_model = poly1d(polyfit(x, y, 3))
# my_line = linspace(1, 22, 100)

# plot.scatter(x, y)
# plot.plot(my_model(my_line))
# plot.show() 

print("Precision score: %f"%(r2_score(y, my_model(x))))
print(my_model(17))