import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np

def aver(p):
	return p[0] + p[1] + p[2] + p[3] * 2

def count(a, b):
	f = open("scores.csv")
	reader = csv.reader(f)
	return sum([1 for row in reader if row[0].isdigit() and a * 5 <= aver(list(map(int, row))) < b * 5])

plt.title('the Complement of Every student')
plt.ylabel('Complement\nindex', loc = 'top', rotation = 0)
plt.xlabel('Student id')
f = open("scores.csv")
reader = csv.reader(f);
cnt = 0

plt.xlim(0, 43)
plt.xticks(np.arange(1, 42, 1))
plt.ylim(0, 1)
for row in reader:
	if row[0].isdigit():
		cnt += 1
		plt.plot(cnt, aver(list(map(int, row))) / 500, 'ro')
plt.axhline(0.7)
plt.show()
