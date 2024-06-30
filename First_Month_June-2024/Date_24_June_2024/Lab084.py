# Leetcode program = sum of digits

number = int(input("Enter a number: "))


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(number))

sum_digits = lambda n1: 0 if n1 == 0 else n1 % 10 + sum_digits(n1 // 10)
print(sum_digits(number))

number1 = 12345
n2 = number1 // 10
q1 = number1 % 10

print(n2, q1)


# without recursion

number1 = int(input("Enter a number: "))


def sum_digits1(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n = n // 10
    return sum_digit


print(sum_digits1(number1))
