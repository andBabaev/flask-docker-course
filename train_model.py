import numpy as np

import sklearn
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump

iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target

iris = datasets.load_iris()
clf = KNeighborsClassifier()

clf.fit(iris.data, iris.target_names[iris.target])
dump(clf, 'knn.pkl') 