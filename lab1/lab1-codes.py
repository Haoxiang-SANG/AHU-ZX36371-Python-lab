def is_double(x):
	cnt = 0
	for a in x :
		if a == '.':
			cnt += 1
		if '0' <= a <= '9' or a == '.' :
			continue;
		else :
			return False;
	if cnt == 0 or cnt == 1 :
		return True
	else :
		return False

def calc(a, b, c):
	delta = b * b - 4 * a * c
	if abs(delta) < 1e-6 :
		#print("1", -b / (2 * a), sep = '\n')
		return [-b / (2 * a)]
	elif delta > 0 :
		#print("2", (-b - math.sqrt(delta)) / (2 * a), (-b + math.sqrt(delta)) / (2 * a), sep = '\n')
		return [(-b - math.sqrt(delta)) / (2 * a), (-b + math.sqrt(delta)) / (2 * a)]
	elif delta < 0 :
		#print("0")
		return []

def printans(a, b, c):
	print("a = %f" % a, "b = %f" % b, "c = %f" % c, sep = ', ')
	anslist = calc(a, b, c)
	print(len(anslist))
	for x in anslist:
		print("%.3f" % x)

	

import math

'''
while 1:
	a = input()
	if (is_double(a) == True) :
		break;
	print("invalid input ! Please regive number A")

while 1:
	b = input()
	if (is_double(b) == True) :
		break;
	print("invalid input ! Please regive number B")

while 1:
	c = input()
	if (is_double(c) == True) :
		break;
	print("invalid input ! Please regive number C")
'''

tot = input()
a, b, c = tot.split()

a = float(a)
b = float(b)
c = float(c)

if a == 0 :
	print("The equation isn't a quadratic!")
else :
	printans(a, b, c)
