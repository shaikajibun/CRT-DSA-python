"""Question 2: Student Class
Create a class called Student.
Attributes:
name
roll_no
branch
Method:
display()
Create 3 student objects and display details."""

class Student:
    def __init__(self,name,roll_no,branch):
        self.name=name
        self.roll_no=roll_no
        self.branch=branch
    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)
        print("branch:",self.branch)
s1=Student("ravi",15,"cse")
s2=Student("ajibun",12,"ece")
s3=Student("dhana",11,"it")
s1.display()
s2.display()
s3.display()