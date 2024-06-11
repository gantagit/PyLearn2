# functions
# In built functions
# print(), max(), min(), ........

# string functions

name = "Amit"
print(name)
print(type(name))
print(id(name)) # stored location  i.e. memory address where it is stored
print(len(name)) # length always starts from 1
print(name.count('A')) # count the number of A  # Python is case sensitive
print(name.count('a')) # count the number of a

name = name.lower()  # convert to lower case
print(name)

print(name.count('a')) # count the number of a #  here the Amit is changed to amit due to lower()
print(name.count('A')) # count the number of A
