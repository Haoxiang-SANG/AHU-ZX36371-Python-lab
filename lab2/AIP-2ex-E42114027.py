import math

class Vector3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, other):
		return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
	def __sub__(self, other):
		return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
	def len(self):
		return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
	def __mul__(self, k):
		return Vector3D(self.x * k, self.y * k, self.z * k)
	def __truediv__(self, k):
		return Vector3D(self.x / k, self.y / k, self.z / k)
	def output(self):
		print("(%f, %f, %f)" % (self.x, self.y, self.z))

a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
c = 3

(a + b).output()
(a - b).output()
(a * c).output()
(a / c).output()
print("a 的长度为 %f。" % a.len())
