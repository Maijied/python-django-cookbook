'''
Classes In Python =>
In Python, a class is a blueprint for creating objects (a particular data structure), providing initial values for state
(member variables or attributes), and implementations of behavior (member functions or methods). A class can be defined
by keyword class followed by the name of the class. The class definition usually contains a number of function
definitions (methods) which operate on instances of the class. Class definitions create a new local namespace where all
its attributes are defined.

Attributes are data stored inside a class or instance and represent the state or quality of the class or instance.
In Python, there are two types of attributes: Class attributes and instance attributes. Class attributes are shared by
all instances of the same class, while instance attributes are unique to each instance.

Methods are functions that belong to a class and define how instances of that class should interact with each other and
with external code. Methods can be used to get or set the value of an attribute, perform some computation, or call other
methods within the same object.
'''


# This code creates an instance of the class MyClass and assigns it to the variable p1. It then prints the value of
# the attribute x, which is 5.
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)  # 5


# This code creates a Person object with the given name and age. It then prints out the name and age of the Person
# object.
class Person:
    def __init__(self, name, age):
        # pass
        self.name = name
        self.age = age


name = input('Enter Your Name : ')
age = int(input('Enter Your Name : '))
PersonObj = Person(name, age)
# del PersonObj.age  # Delete Object
print(PersonObj.name + " And", PersonObj.age)  # MaJHi And 71
