# print all the numbers in a given range using for loop and break
start = 0
stop = 100
break_point = int(input("Enter the number to break the loop:\t"))

for count in range(start, stop):
    print(count)
    if count == break_point:
        break
