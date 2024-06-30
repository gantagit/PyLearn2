# Tuple - Collection of items

a = 56

# b, c = (78, 99, 80) this will give error as there are more values
b, c = (78, 99)  # unpacking of tuple

print(a)
print(b)
print(c)

# search in tuple

cities1 = ("Delhi", "Mumbai", "Chennai", "Kolkata")
print("Delhi" in cities1)  # this will be True
print("delhi" in cities1)  # this will be false due to case sensitive

print("London" in cities1)

cities2 = ("Delhi", "Mumbai", "Chennai", "Kolkata", "London")

print("London" in cities2)  # in is used to find the items in tuple
