'''
This code will prompt the user to input an integer value. If the user inputs an integer, the code will print out
the value of x. If the user inputs a non-integer value, it will print out a message saying that x is not an integer
and to try again. Finally, it will print out a message saying "try except finished." regardless of what the user
inputs.
'''
try:
    x = int(input("Input an integer : "))
    print('x : ', x)
except ValueError:  # Unexpected value -> ValueError
    print('x is not integer value... Please try again.')
finally:
    print('try except finished.')
