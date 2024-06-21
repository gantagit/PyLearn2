# functions with examples
def arithmetic_operations(a, b):
    print("Addition is: ", a + b, "\nSubtraction is: ", a - b,
          "\nMultiplication is: ", a * b, "\nDivision is: ", a / b, "\nModulus is: ", a % b)


m, n = float(input("Enter value for m :\t ")), float(input("Enter value for n :\t"))
arithmetic_operations(m, n)
