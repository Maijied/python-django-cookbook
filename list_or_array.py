countries = ['Ghana', 'America', 'Canada', 'Greece', 'Saudi Arabia', 'UK']
print(countries)  # ['Ghana', 'America', 'Canada', 'Greece', 'Saudi Arabia', 'UK']
print(countries[2][2]) #n
print(countries[0:3]) #['Ghana', 'America', 'Canada']
print(type(countries)) #<class 'list'>
countries[0] = 'Azerbaijan'
print(countries)  # Manipulated list -> ['Azerbaijan', 'America', 'Canada', 'Greece', 'Saudi Arabia', 'UK']
print(countries[-2])  # reverse index -> Saudi Arabia
print(countries[-2:])  # reverse index -> ['Saudi Arabia', 'UK']

# List constructor
another_countries_list = list(('Hello', 1, True, 'Bro'))  # List constructor
print(another_countries_list)  # ['Hello', 1, True, 'Bro']

# List merge
list1 = [1, 2, 3, 4, 5]
list2 = ['One', 'Two', 'Three', 'Four', 'Five', 'Five']
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 'One', 'Two', 'Three', 'Four', 'Five']
list2.append('Six')
print(list2)  # ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
list2.insert(0, 'Zero')
print(list2)  # ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six']
list2.remove('One')
print(list2)  # ['Zero', 'Two', 'Three', 'Four', 'Five', 'Six']
# list2.clear()
print(list2)  # []
print(list2.index('Zero'))  # 0
print(list2.count('Five'))  # 2
list3 = [9, 5, 8, 1, 3, 0, 2]
list3.sort()
print(list3)  # [0, 1, 2, 3, 5, 8, 9]
list3.reverse()
print(list3)  # [9, 8, 5, 3, 2, 1, 0]
list3 = list1.copy()
print(list3)  # [1, 2, 3, 4, 5, 'One', 'Two', 'Three', 'Four', 'Five', 'Five']
list3.pop()
print(list3)  # [1, 2, 3, 4, 5, 'One', 'Two', 'Three', 'Four', 'Five']
del list3[0]
print(list3)  # [2, 3, 4, 5, 'One', 'Two', 'Three', 'Four', 'Five']









