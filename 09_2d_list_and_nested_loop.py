'''
2D List =>
A 2D list is a list of lists. It is used to store data in a tabular format, where each row represents a new list and
each column represents an element in the list. A 2D list can be used to represent a matrix or table of values.
'''

# This code creates a list of lists. The list contains three sub-lists, each containing three elements. The elements
# in the sub-lists are integers ranging from 1 to 9.
my_list = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
           ]
print(my_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list[1])  # [4, 5, 6]
print(my_list[2][1])  # 8

'''
Nested loop =>
Nested loops in Python are used to execute multiple loops within each other. This allows for more complex operations to 
be performed, such as looping through a list of lists or looping through a dictionary. Nested loops can also be used to 
iterate over multiple data structures at the same time.
'''
# Nested Loops -> This code iterates through each item in the list 'my_list' and then iterates through each row in the
# item. For each row, it prints the row.
for item in my_list:
    for row in item:
        print(row)
