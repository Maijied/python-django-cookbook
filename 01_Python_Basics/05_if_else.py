"""
If-else statements in Python are used to execute different code depending on whether a certain condition is true or
false. They are used to control the flow of a program, allowing it to make decisions and perform different actions based
on the user's input or other conditions.
"""

a = 4
b = 3
c = 3
d = True
e = False

# This code compares the values of two variables, a and b. If the value of a is greater than b, it prints a statement
# saying that a is greater than b. Otherwise, it prints a statement saying that a is less than b.
if a > b:
    print(str(a) + ' is greater than ' + str(b))
else:
    print(str(a) + ' is less than ' + str(b))

# This code compares the values of variables b, c, d, and e. If b is equal to c, it prints "b is equal to c". If d is
# equal to e, it prints "d == c". If d is not less than e, it prints "d !< c". Otherwise, it prints "d != c".
if b == c:
    print('b is equals to c')
elif d == e:
    print('d == c')
elif d < e:
    print('d !< c')
else:
    print('d != c')  # d != c

# another example-> This Python code checks if a person is a boy and if they are short. If both conditions are true,
# it prints out "He is a boy and Short too". Otherwise, it prints out "He is not a boy".
boy = True
short = True

if boy == True and short == False:
    print('He is a boy but short.')
elif boy == False or short == False:
    print('He is not a boy')
elif boy == True and short == True:
    print("He is a boy and Short too")  # He is a boy and Short too

# Another Example This code checks the type of given value and prints out a corresponding string. It first takes an
# input from the user and stores it in the variable 'value'. Then, it uses an if-elif statement to check the type of
# 'value' and prints out a corresponding string.
value = input("Please Enter a value : ")
# value = 1
if type(value) == str:
    print('String')
elif type(value) == int:
    print("Number")
elif type(value) == bool:
    print('Boolean')
elif type(value) == list:
    print('List')
elif type(value) == tuple:
    print('Tuple or Obj')
else:
    print('We dont recognize! the data type of' + value)
