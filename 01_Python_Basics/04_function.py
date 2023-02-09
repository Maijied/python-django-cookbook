'''
Function =>
In Python, a function is a group of related statements that performs a specific task. Functions help break our program
into smaller and modular chunks. As our program grows larger and more complex, functions make it more organized and
manageable. Furthermore, it avoids repetition and makes code reusable.
'''


# This code defines a function called greetings_function that takes one parameter, name. When the function is called,
# it prints out a welcome message with the name passed in as an argument.
def greetings_function(name):
    print("Welcome " + str(name))


greetings_function('Majhi')  # Welcome Majhi
greetings_function(71)  # Welcome, 71

# This code prints a welcome message to the user, using the first argument passed to the function as their name and
# the second argument as their age.
def aboutme(*names):
    print('Welcome ' + str(names[0]) + ' You are ' + str(names[1]) + ' years old!')


aboutme('Majhi', 25)  # Welcome Majhi You are 25 years old!

# This code prints a welcome message with the name and age of the person passed as parameters. The parameters are
# "name" and "age". The code prints "Welcome Majhi_Bhai You are 50 years old!"
def multiparameter(name, age):
    print('Welcome ' + str(name) + ' You are ' + str(age) + ' years old!')


multiparameter(name='Majhi_Bhai', age=50)  # Welcome Majhi_Bhai You are 50 years old!

# This code takes two parameters, name and age,
# from the user and prints out a welcome message using those parameters.
def parameterfrominput(name, age):
    print('Welcome ' + str(name) + ' You are ' + str(age) + ' years old!')


name = input("Whats Your Name : ")
age = input("How Old Are You : ")
parameterfrominput(name, age)  # Welcome Shamim You are 12 years old!
