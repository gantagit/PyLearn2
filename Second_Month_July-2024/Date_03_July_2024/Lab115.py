# Exception Handling

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
else:
    print("Result: ", result)
finally:
    print("End of the program")
