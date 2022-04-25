bark = 'wang'

class Pet:
	def __init__(self, name, age):
		self.__name = name
		self.__age  = age
	def show(self):
		print("我的名字是%s，我今年 %d 岁！" % (self.__name, self.__age))
	def makeSound(self):
		print(bark)

class Dog(Pet):
	def __init__(self, name, age, breed):
		Pet.__init__(self, name, age)
		self.__breed = breed
	def show(self):
		Pet.show(self)
		print("我的品种是%s！" % self.__breed)
	def makeSound(self):
		print((bark + '...') * 3)

y = Pet('旺财', 3)
y.show()
y.makeSound()

x = Dog('二哈', 2, '哈士奇')
x.show()
x.makeSound()
