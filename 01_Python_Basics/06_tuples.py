'''
Tuple =>
A tuple is an immutable sequence of values. It is similar to a list, but the values in a tuple cannot be changed once
they are created. Tuples are often used to store related pieces of information, such as a person's name and age. They
can also be used to return multiple values from a function.
'''

# This code creates a tuple containing the numbers 1, 2, and 3. A tuple is an immutable sequence of values that can
# be accessed by index.
three_numbers = (1, 2, 3)
print(three_numbers)  # (1, 2, 3)
print(type(three_numbers))  # <class 'tuple'>

'''
This code creates a tuple containing four elements: an integer (1), a string ("One"), a boolean (True), and another 
integer (2). Tuples are immutable sequences of objects, meaning that the elements cannot be changed once they are 
created.
'''
randomType = tuple((1, 'One', True, 2))
print(randomType)  # (1, 'One', True, 2)
print(randomType[1])  # One


