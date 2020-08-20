import pandas
from sklearn import linear_model

df = pandas.read_csv("dataset/cars.csv")

X = df[["Weight", "Volume"]]
y = df["CO2"]

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300ccm:
predictedCO2 = regr.predict([[3300, 1300]]) 

print(predictedCO2)
print(regr.coef_) 