# print all the even or odd numbers in a given range using list based onm the input number
number = int(input("Enter the number:\t"))

start = 0
stop = 100
step = 2

if number % 2 == 0:
    print("number is {} so the even number list will be printed till the range :\t".format(number))
    print(list(range(start, stop, step)))
else:
    print("number is {} so the odd number will be printed till the range :\t".format(number))
    print(list(range(start + 1, stop, step)))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# print all the even or odd numbers in a given range using for loop based onm the input number
number = int(input("Enter the number:\t"))
start = 0
stop = 100
step = 2

if number % 2 == 0:
    print("number is {} so the even number list will be printed till the range :\t".format(number))
    for count in range(start, stop, step):
        print(count)
else:
    print("number is {} so the odd number will be printed till the range :\t".format(number))
    for count in range(start + 1, stop, step):
        print(count)
