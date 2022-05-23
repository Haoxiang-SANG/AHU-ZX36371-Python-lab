from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data_diabetes = load_diabetes(return_X_y = 1);
n = len(data_diabetes[1])

L = list(zip(data_diabetes[0], data_diabetes[1]))

import random
random.shuffle(L)
L1 = L[0:(int)(len(L) * 0.8)]
L2 = L[(int)(len(L) * 0.8):]

for i in range(10):
	x = [record[0][i] for record in L1]
	y = [record[1] for record in L1]
	plt.subplot(2, 5, i + 1)
	plt.plot(x, y, 'ro')
	plt.title("Plot %d" % i)

plt.show()

regr = LinearRegression()
regr.fit([record[0] for record in L1], [record[1] for record in L1])

for i in range(10):
	plt.bar(i, regr.coef_[i])
plt.show()

error1 = mean_squared_error([record[1] for record in L1], regr.predict([record[0] for record in L1]))
error2 = mean_squared_error([record[1] for record in L2], regr.predict([record[0] for record in L2]))

print("error1 = %.5f\nerror2 = %.5f\n" % (error1, error2))
