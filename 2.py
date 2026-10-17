class Student:
    name = "Harshi"
    age = 20
student1 = Student()
print(student1.name)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student1 = Student("Harshi", 20)
        print(student1.name)
        print(student1.age)