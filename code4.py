"""Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name Anna; and gradeA
Print the grade of s1
Change the grade of s1 to B
Print the updated grade"""
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s1=Student('Anna','A')
s1.grade='B'
print(s1.grade)