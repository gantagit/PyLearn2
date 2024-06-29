# Recursion
# from math import factorial

# recursions is a programming technique to call a function itself to solve a problem

# key concepts
# 1. base case
# 2. recursive case

num = int(input("Enter a number: "))

# fact using lambda
fact = lambda n: 1 if n == 0 else n * fact(n - 1)
print(fact(num))


# fact using function
def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n - 1)


print(fact(num))

# 0 return 1
# 1 return ( here 1 = (n-1 = 1  because we mentioned when n == 0 return 1))
# 2 return ( here 2 * (n-1 = 1)
# 3 return ( here 3 * (n-1 = 2)
# 4 return ( here 3 * (n-1 = 3)
# 5 return ( here 3 * (n-1 = 4)
