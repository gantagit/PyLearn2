# Conditions
# Program to compare two float numbers
# If-elif-else loop

a = float(input("Enter a number: \n"))
b = float(input("Enter another number: \n"))

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# The above can be done using max() function as well
print("Maximum of {} and {} is {}".format(a, b, max(a, b)))

#  +++++++++++++++++++++++++++++++++++++++++++++++++++++
# Program to find the smallest of three float numbers
x = float(input("Enter a number: \n"))
y = float(input("Enter another number: \n"))
z = float(input("Enter another number: \n"))

if x < y and x < z:
    print("x is the smallest")
elif y < x and y < z:
    print("y is the smallest")
else:
    print("z is the smallest")

# The above can be done using max() function as well
print("Maximum of {} and {} and {} is {}".format(x, y, z, min(x, y, z)))
