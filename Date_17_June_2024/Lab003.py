# functions with examples
def arithmetic_operations(a, b):
    print("Addition of {} and {} is: ".format(a, b), a + b)
    print("Subtraction of {} and {} is: ".format(a, b), a - b)
    print("Multiplication of {} and {} is: ".format(a, b), a * b)
    print("Division of {} and {} is: ".format(a, b), a / b)
    print("Modulus of {} and {} is: ".format(a, b), a % b)


m, n = float(input("Enter value for m :\t ")), float(input("Enter value for n :\t"))
arithmetic_operations(m, n)
arithmetic_operations(10, 3)
