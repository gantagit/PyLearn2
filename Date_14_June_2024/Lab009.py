# functions with examples
def arithmetic_operations(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b
    print("Addition is: ", add)
    print("Subtraction is: ", sub)
    print("Multiplication is: ", mul)
    print("Division is: ", div)
    print("Modulus is: ", mod)
    return add, sub, mul, div, mod


m = float(input("Enter a number: "))
n = float(input("Enter another number: "))
arithmetic_operations(m, n)
