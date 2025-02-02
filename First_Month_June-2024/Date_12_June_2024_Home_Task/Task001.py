# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
#
# 	Input = 2024
# 	Output = Leap year
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
year = int(input("Enter a year \t"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
