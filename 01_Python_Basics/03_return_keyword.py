"""
Return keyword =>
The return keyword in Python is used to exit a function and return a value. It can be used to return multiple
values as well. It is also used to end the execution of a loop.
"""


# This python code defines a function called addfunction() that returns the sum of 5 and 10 when called. When the code
# is run, it prints out the result of 15.


def addfunction():
    return 5 + 10


print(addfunction())  # 15


# This code prompts the user to enter two numbers, stores them in variables num1 and num2, and then passes them as
# parameters to the parameterbasedaddfun function. The function adds the two numbers together and returns the result
# which is then printed.

def parameterbasedaddfun(num1, num2):
    return num1 + num2


num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
print(parameterbasedaddfun(num1, num2))  # 100+50 -> 150
