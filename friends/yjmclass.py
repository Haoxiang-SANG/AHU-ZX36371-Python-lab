class Pet:
    def __init__(self,name,age,sound):
        self.__name=name
        self.__age=age
        self.__sound=sound
    def show(self):
        print('Name=',self.__name,',Age=',self.__age)
    def makeSound(self): 
        print('MakeSound=',self.__sound)
        
class Dog(Pet):
    def __init__(self,name,age,sound,breed):
        Pet.__init__(self, name, age, sound);
        self.__breed = breed
    def show(self):
        Pet.show(self)
        print('breed=',self.__breed)

D=Dog('lucky', 6, 'wang...wang...wang...', '哈士奇')
D.show()
D.makeSound()
