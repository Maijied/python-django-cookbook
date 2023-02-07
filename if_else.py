a = 4
b = 3
c = 3
d = True
e = False

if a>b:
    print(str(a)+ ' is greater than '+ str(b))
else:
    print(str(a)+ ' is less than '+ str(b))

if b==c:
    print('b is equals to c')

if d == e:
    print('d == c')
elif d < e:
    print('d !< c')
else:
    print('d != c') # d != c

# another example
boy = True
short = True

if boy == True and short == False:
    print('He is a boy but short.')
elif boy == False or short == False:
    print('He is not a boy')
elif boy == True and short == True:
    print("He is a boy and Short too") # He is a boy and Short too


# Another Example
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
    print('Tiple or Obj')
else:
    print('We dont recognize!')

