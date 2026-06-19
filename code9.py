"""Question 3: Car Class
Create a class called Car.
Attributes:
brand
color
Method:
start_engine()
Output:
Toyota car started"""
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start_engine(self):
        print(self.brand,"car started")
c1=Car("toyota","white")
c1.start_engine()