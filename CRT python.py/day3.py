class Student:
    def __init__(self,name,age,rollno):
        self.name=name 
        self.__age=age
        self.__rollno=rollno
    def study(self):
        print('reading')
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')
ajibun=Student('ajibun',21,'L12')
print(ajibun.name)
print(ajibun.__age)
print(ajibun.__rollno)
ajibun.study()
ajibun.eat()
ajibun.sleep()