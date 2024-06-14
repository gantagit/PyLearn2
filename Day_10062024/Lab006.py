# Arithmetic Operators
# +,-,/,*,%
# Addition   +
# Subtraction -
# Multiplication *
# Division /, This always gives float
# Modulus %, This always gives remainder
# Exponent **, This gives power of a number
# Floor Division //, This always gives integer and Quotient

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a ** b = ", a ** b)  # power of a number
print("a ++ b = ", pow(a, b))  # power of a number
print("a // b = ", a // b) # returns integer and Quotient

