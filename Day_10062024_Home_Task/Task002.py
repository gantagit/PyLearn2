# Develop a python script that calculates the square and cube of a given number,
# Example num = 2, square is 4, cube is 8

# solution for first problem of this task
import math

number = float(input("Enter a number: "))
print("Square of a number is ", math.pow(number, 2))
print("Cube of a number is ",  math.pow(number, 3))

# Using Ternary Operator, Create a program that takes two numbers as input and prints 4
# whether the first number is greater than, less than, or equal to the second number

# solution for second problem of this task
# a = int(input("Enter value for variable a: \t"))
# b = int(input("Enter value for variable b: \t"))
a, b = int(input("Enter value for variable a : \n")), int(input("Enter value for variable b : \n"))
print("a is greater than b" if a > b else "a is lesser than b" if a < b else "a is equal to b")

