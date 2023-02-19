# Basic calculator program
num1 = int(input('Enter your first number : '))
num2 = int(input('Enter your second number : '))
op = input('Enter operator : ')

if op == '+':
    print('The addition is : ', num1+num2)
elif op == '-':
    print('The subtraction is : ', num1-num2)
elif op == '*':
    print('The multiplication is : ', num1 * num2)
elif op == '/':
    print('The division is : ', num1 / num2)
elif op == '%':
    print('The remainder is : ', num1 % num2)
else:
    print('Invalid Operator!')