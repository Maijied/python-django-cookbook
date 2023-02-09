'''
Python is a high-level, interpreted, general-purpose programming language. It was created by Guido van Rossum and first
released in 1991. Python is easy to learn and its syntax is simple to understand, making it an ideal language for
beginners. It has a wide variety of applications in fields such as web development, data science, scripting, automation,
artificial intelligence, and more.
'''

# import built-in functions
from math import *

# Print Func
print("Hello World")
print("My name is MaJHi, My age is", 100)  # Print Int

# Variable
name = 'MaJHi'  # String
print(name)
age = 18  # Int
print(age)

# Concat
print(name + ' is a dev.')  # String Concate
print(name, ' is', age)  # Integer Concate

# Let's Play With String
print('Hi \n How are you?')  # New Line
print('My name in uppercase', name.upper())  # Uppercase
print('My name in lowercase', name.lower())  # Lowercase
print('My name is in lowercase or uppercase?', name.islower(),
      name.isupper())  # Bool check isLowercase or isUppercase -> False and False
print('My name is in lowercase comparison?', name.lower().islower())  # Bool check isLowercase or isUppercase ->true
print(len(name))  # Length count
print('Index number of i from name', name.index('i'))  # Index of char
print('Replace character from string', name.replace('i', 'ii'))  # Replace character

# Let's play with number's
number = 69
print(68)
print(number)
print(number - 9.81)  # Fractional number
number2 = str(number)
print(number2 + ' is my number')  # string concate
print(number, ' is my number')  # number concate
print(number, ' is my number')  # number concate
minusNumber = -69
print(abs(minusNumber))  # Absolute Number
print(max(minusNumber, number))  # max Number
print(min(minusNumber, number, 100, 50, 101))  # min Number
print(round(9.81))  # round Number
print(bin(334))  # binary string Number

# Math functions
print(sqrt(16))

# input
inputName = input('Whats your name:')
inputAge = int(input('Whats your age:'))
print(inputName)
print(inputAge)
print('Your name is ' + inputName + ' And your are ', inputAge, ' years old.')


# Comments
# print('Comment') #Single line comment

# Multi line comment
'''
def my_fun():
    print('Hi Comment')
'''
