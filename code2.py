"""The __init__() Method
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary 
when the object is being created.

inside the editor, complete the following steps:
Create a class called Dog
Add an __init__ method with parameters name and age, and store them as properties using self
Add a method called bark that prints the dogs name followed by says Woof!
Create an object d1 of the Dog class with name Buddy and age 3
Call the bark method on d1"""
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(self.name,"says Woof! Woof!")
Pet=Dog('Buddy',3)
Pet.bark()