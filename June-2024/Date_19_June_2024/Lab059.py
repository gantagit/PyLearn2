# Functions Scope and Lifetime
# lambda expression with example

n = int(input("Enter a number: "))


# doubling a number using function
def double_number(number):
    return number * 2


result = double_number(n)
print(result)

# ++++++++++++++++++++++
# lambda expression is used for doing the task in a single line
func_double_numbers = lambda numbers: numbers * 2  # this is a lambda expression
print(func_double_numbers(n))
