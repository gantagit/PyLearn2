# ✅ #4. Fibonacci series
# # 0,0+1, 0+1+1,
#
# n = 7
#
# 0, 1, 2, 3, 5, 8, 1
num_1 = 0
num_2 = 1
fact = 0
total_range = int(input("Enter the total range : \t"))

for i in range(total_range):
    fact = num_1 + num_2
    num_1 = num_2
    num_2 = fact
    print(fact)