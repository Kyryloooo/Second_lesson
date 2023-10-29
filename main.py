class Test:
    a=1
    b=1
test1=Test()
test2=Test()

test1.a = 25

print(test1.a)
print(test2.a)





class Student:
    def __init__(self, name="Vasya", age=18):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old!")


first_student = Student("Petya", 16)
second_student = Student("Anna", 21)
third_student = Student()
first_student.say_hi()
second_student.say_hi()
third_student.say_hi()
