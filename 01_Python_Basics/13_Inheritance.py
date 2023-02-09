'''
Inheritance in Python is the process by which one class can inherit the attributes and methods of another class.
This allows for code reuse and efficient memory management. Inheritance is a powerful feature in object-oriented
programming, as it allows classes to be related to each other in a hierarchical manner.
'''

from inherit import Student


class Person(Student):
    pass


p1 = Person()
print(p1.name)  # Tamas
