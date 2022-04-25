class Pet:
    def _init_(self):
        self.__name=name
        self.__age=age
        self.sound=sound
    def show(self):
        print('Name=',self.name,',Age=',self.age)
    def makeSound(self): 
        print('MakeSound=',self.sound)
        
class Dog(Pet):
    def _init_(self,breed):
        self.__breed=breed

D=Pet()
D.name='lucky'
D.age=6
D.sound='wang...wang...wang...'
breed='哈士奇'
D.show()
D.makeSound()
