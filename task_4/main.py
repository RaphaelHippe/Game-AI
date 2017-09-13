from sklearn import tree
from sklearn.externals.six import StringIO

import pydot
features = ["visible", "distance", "armed"]
class_names = ["True", "False"]
X = [
[0,0,0],
[0,0,1],
[0,1,0],
[0,1,1],
[0,2,0],
[0,2,1],
[1,0,0],
[1,0,1],
[1,1,0],
[1,1,1],
[1,2,0],
[1,2,1]
]
# X = [[0,0], [1,1]]
Y = [1,0,0,0,0,0,1,1,1,1,0,0]
# Y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
dot_data = StringIO()

tree.export_graphviz(clf,out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
