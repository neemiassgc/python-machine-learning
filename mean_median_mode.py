from data import dataset
from numpy import mean, median
from scipy import stats

# mean
print(mean(dataset))

# median
print(median(dataset))

# mode
print(stats.mode(dataset))