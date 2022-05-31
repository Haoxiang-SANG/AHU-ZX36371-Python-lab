from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
 
mnist = fetch_openml('mnist_784', as_frame = False)

x, y = mnist['data'], mnist['target']
x_train, x_test, y_train, y_test = train_test_split(mnist['data'], mnist['target'], test_size = 1 / 7)

x_draw, _, y_draw, _ = train_test_split(x_train, y_train, train_size = 32)

for i in range(32):
	plt.subplot(4, 8, i + 1)
	plt.imshow([x_draw[i][j:j+28] for j in range(0, 784, 28)])
	plt.title("truth = %d" % int(y_draw[i]))
	plt.axis('off')
plt.show()

clf = SGDClassifier(loss = 'log', verbose = 2)
clf.fit(x_train, y_train)

acc1 = clf.score(x_train, y_train)
acc2 = clf.score(x_test, y_test)
print(acc1, acc2)

from sklearn.metrics import confusion_matrix
cmat = confusion_matrix(y_train, clf.predict(x_train))
print(cmat)

x_draw, _, y_draw, _ = train_test_split(x_test, y_test, train_size = 32)
y_drawp = clf.predict(x_draw)
for i in range(32):
	plt.subplot(4, 8, i + 1)
	plt.imshow([x_draw[i][j:j+28] for j in range(0, 784, 28)])
	plt.title("truth = %d\nMy predict = %d" % (int(y_draw[i]), int(y_drawp[i])))
	plt.axis('off')
plt.show()
