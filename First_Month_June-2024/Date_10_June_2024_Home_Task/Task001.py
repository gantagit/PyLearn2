# 1) Explain the difference between = operator and == operator
# here = operator is used for assign a literal to a variable
a = float(input("Enter value for a : \n"))
b = float(input("Enter value for b : \n"))
# here == operator is used for comparison
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2) What does the ** operator do in python and how is it used
# Here ** is operator is used as power
print("a power of b is ", (a ** b))
# the above line is similar to
# print("a power of b is ", math.pow(a,b))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 3) What does the ^ operator do in python, and in what context is it commonly used
# ^ is a bit wise XOR operator
# XOR operator is used to perform bitwise XOR operation on the operands
# example x = 5 (101 in binary) and y = 3 (011 in binary)
# then x ^ y = 6 (110 in binary)
x = 5
y = 3
print("XOR of {},{} =  {}".format(x, y, x ^ y))  # Output: XOR of a, b = 6.format(x, y, x^y))
