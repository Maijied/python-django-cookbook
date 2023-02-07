def greetings_function(name):
    print("Welcome "+str(name))

greetings_function('Majhi')  # Welcome Majhi
greetings_function(71)  # Welcome 71


def aboutme(*names):
    print('Welcome '+str(names[0])+' You are '+ str(names[1])+ ' years old!')

aboutme('Majhi', 25) # Welcome Majhi You are 25 years old!

def multiparameter(name, age):
    print('Welcome '+str(name)+' You are '+ str(age)+ ' years old!')

multiparameter(name='Majhi_Bhai', age=50)  #Welcome Majhi_Bhai You are 50 years old!

def parameterfrominput(name, age):
    print('Welcome ' + str(name) + ' You are ' + str(age) + ' years old!')

name = input("Whats Your Name : ")
age = input("How Old Are You : ")
parameterfrominput(name,age)  #Welcome Shamim You are 12 years old!



