# functions

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
fact_number = int(input("Enter a number to find its factorial: "))
if fact_number < 0:
    print(" factorial cannot exist for negative numbers")
elif fact_number == 0:
    print(" factorial of 0 is 1")
else:
    for i in range(1, fact_number, 1):
        fact_number *= i

print(fact_number)


# ++++++++++++++++++++++++++++++++++++++
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number to find its factorial: "))

print(factorial(n))
