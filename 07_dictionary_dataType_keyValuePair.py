'''
Dictionary =>
A dictionary is a collection of key-value pairs. It is an unordered and changeable data type. Dictionaries are used
to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary
holds key:value pair. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a
‘comma’.
'''

# This code creates a dictionary called my_dictionary with five key-value pairs. The keys are 'name', 'age',
# 'nationality', 'is_male' and 'qualifications'. The values associated with each key are a string, an integer,
# a string, a boolean and a list respectively.
my_dictionary = {
    'name': 'Majhi',
    'age': 71,
    'nationality': 'Bangladeshi',
    'is_male': True,
    'qualifications': ['PSC', 'SSC', 'HSC', 'BSC', 'MSC']
}
print \
    (my_dictionary)  # {'name': 'Majhi', 'age': 71, 'nationality': 'Bangladeshi', 'is_male': True, 'qualification': ['PSC', 'SSC', 'HSC', 'BSC', 'MSC']}
print(type(my_dictionary))  # <class 'dict'>
print(my_dictionary['qualifications'])  # Majhi
print(my_dictionary['qualifications'][0])  # PSC
x = my_dictionary['qualifications']
print(x)  # ['PSC', 'SSC', 'HSC', 'BSC', 'MSC']
