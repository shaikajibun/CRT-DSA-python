class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(self.name,"says bow! bow!!")
pet=Dog('Buddy')
pet.bark()