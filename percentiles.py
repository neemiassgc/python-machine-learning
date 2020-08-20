from numpy import percentile
from data import ages

print("75 percentile is %s"%(percentile(ages, 75)))
print("90 percentile is %s"%(percentile(ages, 90)))