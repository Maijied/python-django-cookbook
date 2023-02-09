'''
While =>
A while loop in Python is a type of loop that will execute a set of statements as long as a given condition is true.
It will repeat the statements until the condition becomes false.
The syntax for a while loop is: while <condition>: <statements>
'''

# This code prints the numbers 1 through 6. The variable i is initialized to 1 and then the while loop runs as long
# as i is less than 6 or equal to 6. Inside the loop, the value of i is printed and then incremented by 1.
i = 1
while i < 6 or i == 6:
    print(i)  # 1 2 3 4 5 6
    i += 1
# 1
# 2
# 3
# 4
# 5
# 6

'''
For Loop =>
A for loop in Python is a type of loop that iterates over a sequence of items, such as a list or a string. It executes 
a set of statements for each item in the sequence. The syntax for a for loop is:

for item in sequence:
    statement(s)
'''
# This code will print each letter of the string 'hello' on a separate line.
for letter in 'hello':
    print(letter)  # h e l l o

# List Loop -> This code will loop through the list of strings and print each value. When it reaches the string "JU",
# it will print "JU" and then break out of the loop.
my_list = ['BUET', 'SUST', 'DU', 'JU', 'NSU']  # list
for value in my_list:
    print(value)  # BUET SUST DU JU NSU
    if value == 'JU':
        print(value)  # JU
        break

# Key value pair loop -> This code prints out the keys and values of the dictionary "my_dic". It first iterates through
# each key-value pair in the dictionary, then prints out the key and value for each pair.
my_dic = {
    'name': 'Majhi',
    'age': 71,
    'country': 'BD'
}
for key, value in my_dic.items():
    print(key)  # name age country
    print(value)  # Majhi 71 BD

# Range of numbers
# This code prints the numbers 0 through 9 on separate lines.
for x in range(10):
    print(x)  # 1 2 3 4 5 6 7 8 9

# This code will print the numbers 1 through 4, followed by the string "Finished For loops". The for loop will
# iterate through the range of 1 to 5 (not including 5) and print each number. The else statement will execute after
# the for loop has finished, printing "Finished For loops".
for i in range(1, 5):
    print(i)  # 1 2 3 4
else:
    print('Finished For loops')  # Finished For loops
