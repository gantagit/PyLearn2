# Logical Operators
# always return boolean value

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("a > b = ", a > b)  # to check a is greater than b
print("a < b = ", a < b)  # to check a is lesser than b
print("a >= b = ", a >= b)  # to check a is greater than or equal to b
print("a <= b = ", a <= b)  # to check a is lesser than or equal to b
print("a == b = ", a == b)  # to check a is equal to b and it is used for value equality
print("a != b = ", a != b)  # to check a is not equal to b

# more
print("a == b and a > b = ", a == b and a > b)  # to check both conditions are true
print("a == b or a > b = ", a == b or a > b)  # to check either of the conditions are true
print("not(a == b and a > b) = ", not (a == b and a > b))  # to check both conditions are not true
print("not(a == b or a > b) = ", not (a == b or a > b))  # to check either of the conditions are not true
print("a is b = ", a is b)  # to check a is b and it is used for object identity.
