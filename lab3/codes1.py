import csv
import pandas
import matplotlib.pyplot as plt

def aver(p):
	return p[0] + p[1] + p[2] + p[3] * 2

def count(a, b):
	f = open("scores.csv")
	reader = csv.reader(f)
	return sum([1 for row in reader if row[0].isdigit() and a * 5 <= aver(list(map(int, row))) < b * 5])

plt.title('the Distribute of Score')
plt.ylabel('Count', loc = 'top', rotation = 0)
plt.xlabel('Score interval', loc = 'right')
plt.bar('[0, 60)', count(0, 60))
for x in range(3):
	plt.bar('[%d, %d)' % (60 + 10 * x, 70 + 10 * x), count(60 + 10 * x, 70 + 10 * x))
plt.bar('[%d, %d]' % (90, 100), count(90, 101))

plt.show()
