# functions
# In built functions
# print(), max(), min(), ........

# string functions

name = "Amit"  # indexed from 0 to 3
# 0,1,2,3
# a,m,i,t
print(name)
print("data type  of the name is :", type(name))
print("id of the name is :", id(name))  # stored location  i.e. memory address where it is stored
print(len(name)) # length always starts from 1
print(name.count('A'))  # count the number of A  # Python is case sensitive
print(name.count('a'))  # count the number of a

name = name.lower()  # convert to lower case
print(name)
print(len(name))

print(name.count('a'))  # count the number of a #  here the Amit is changed to amit due to lower()
print(name.count('A'))  # count the number of A

# print(name[0],  name[1], name[2], name[3], name[4], sep='-')
print(name[0],  name[1], name[2], name[3], sep='-')

# python - strings are immutable - Can't be changed
name[0] = 'p'
print(name)
#  you can replace the new but it cannot be changed
