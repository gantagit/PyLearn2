# functions for factorial using recursion

# import math
# 5*4*3*2*1

def fact(n):
    # fact_n = 1
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial does not exist for negative numbers"
    else:
        fact_n = n * fact(n - 1)
        return fact_n


result = fact(6)
print(result)

result = fact(5)
print(result)
