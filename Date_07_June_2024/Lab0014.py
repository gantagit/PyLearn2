# strings raw and format
# import os

directory = r'C:\Users\gvk97\PycharmProjects\PyLearn2\Day_07062024'  # here r represents for the raw string
print(f"current directory is {directory}")  # here f represents for format

# drive = os.getcwd()
# print(drive)

# formatting mechanism

num = 90

print(f"the number is {num}")
print(f"the number is {num*2}")
print(f"the number is {num*3}")

b = 1
print("2*{} = {},{}". format(b, b * 2, 3)) # This is just for reference
print("3*{} = {}".format(b,3))  # This is just for reference
