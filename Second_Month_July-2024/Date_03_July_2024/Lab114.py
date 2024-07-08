# Exception Handling


print("Start of the ATM Program")

a = "Invalid input. Please enter a number."

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result: ", result)
except Exception as e:
    print(e)
    # print("Enter a valid integer")

print("End of the ATM Program")
