import pydotplus
from pandas import read_csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plot
from matplotlib import image as plot_img

# Change string values into numerical values:
df = read_csv("./dataset/shows.csv")
df["Nationality"] = df["Nationality"].map({'UK': 0, 'USA': 1, 'N': 2})
df["Go"] = df["Go"].map({"YES": 1, "NO": 0})

features = ['Age', 'Experience', 'Rank', 'Nationality']

# X is the feature columns, y is the target column
X = df[features]
y = df['Go']

# Create a Decision Tree, save it as an image, and show the image
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file = None, feature_names = features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

# img = plot_img.imread('mydecisiontree.png')
# imgplot = plot.imshow(img)
# plot.show() 

print(dtree.predict([[40, 10, 7, 1]])) 