def addfunction():
    return 5+10

print(addfunction()) # 15


def parameterbasedaddfun(num1,num2):
    return num1+num2

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
print(parameterbasedaddfun(num1, num2)) # 100+50 -> 150
