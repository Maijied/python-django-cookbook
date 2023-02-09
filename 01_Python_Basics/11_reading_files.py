'''
Files read write =>
File Reading and Writing in Python is a process of reading and writing data from and to files. It is a very common
operation in programming, as it allows programs to read data from files, write data to files, or both.
'''

# open('countries.txt','a'-> 2nd parameter =>r: read, w: write, a:append, r+: reading and writing
country_file = open('../assets/countries.txt', 'r')
# This code opens a file called 'countries.txt' located in the 'assets' folder and checks if the file is readable.
print(country_file.readable())  # return true or false
# This code reads the first line of a file called "country_file" and prints it out.
print(country_file.readline())  # Ghana
# This code reads the next line of a file called "country_file" and prints it out.
print(country_file.readline())  # Mexico
# print(country_file.readlines())  # ['Colombia\n', 'Canada\n', 'Spain\n', 'Russia\n', 'Azerbaijan\n', 'Ukraine\n']
# print('f'+country_file.readlines()[2])  # Spain
'''
# This code reads the contents of a file called "country_file" line 
# by line and prints each line to the console. Once all lines have been read, the file is closed.
'''
for line in country_file.readlines():
    print(line)  # all names
country_file.close()

'''
# This code opens a file called '../assets/writehere.txt' in write mode also create file if not exists, prompts the user to 
# enter some text,  and then writes that text to the file before closing it.
'''
'''
country_file2 = open('../assets/writehere.txt', 'w')
writeText = input('Write here to save data : ')
country_file2.write(writeText)
country_file2.close()
'''

'''
country_file3 = open('../assets/newfile.txt', 'w')
writeText = input('Write here to save data : ')
country_file3.write(writeText)
country_file3.close()
'''
'''
# This code opens a file called 'writehere.txt' located in the 'assets' folder in append mode, then prompts the user to
# enter some text which is stored in the variable writeText. The code then writes the contents of writeText to the file 
# and closes it.
'''
write_file = open('../assets/writehere.txt', 'a')
writeText = input('Write here to save data : ')
write_file.write('\n' + writeText)
write_file.close()
