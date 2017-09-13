from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
speaking = [
"Hey I am definitely not a hitman",
"Hey I dont carry a gun",
"Hey is this the casino?",
"Hey I am looking to have a good time. Am I in the right spot?",
"Hey my name is Nico Brandt and I study IT in Germany. Please let me in!"
]

speaking_2 = [
"Hey I am Christian Wernet. I am the best! Let me in!",
"Hey I am Jakob Ernst! I am the best! Let me in!",
"Hey I am Johannes Conen! I am the best! Let me in!"
]

gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print "Number of mislabled Points out of a total %d points : %d" % (iris.data.shape[0], (iris.target != y_pred).sum())
