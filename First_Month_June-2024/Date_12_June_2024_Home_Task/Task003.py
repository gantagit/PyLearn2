# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

number_for_factorial = int(input("Enter the number for factorial: "))

if number_for_factorial < 0:
    print("Factorial of negative number doesn't exist")
elif number_for_factorial == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number_for_factorial, 1):
        number_for_factorial *= i
        print(number_for_factorial)
        print(i)
print("Factorial is ", number_for_factorial)

