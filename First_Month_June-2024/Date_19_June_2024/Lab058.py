# Functions Scope and Lifetime
# lambda expression with example
# ++++++++++++++++++++++++++++++++++++++
# sum of two numbers
def sum_two_numbers(a, b):
    return a + b


result = sum_two_numbers(5, 3)
print(result)  # Output: 8

# ++++++++++++++++++++++++++++++++++++++
# sum of two number using lambda
sum_1 = lambda a, b: a + b
print(type(sum_1))  # Output: <class 'function'>
print(sum_1(5, 3))  # Output: 8

# ++++++++++++++++++++++++++++++++++++++
# max of two numbers using lambda
maximum = lambda a, b: max(a, b)
print(maximum(5, 3))  # Output: 5

# ++++++++++++++++++++++++++++++++++++++
# max of two numbers using built in max function
print(max(5, 3))  # Output: 5
