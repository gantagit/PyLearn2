# Loops
# Repeat a block of code multiple times
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
start = int(input("Enter start from index : \n"))
stop = int(input("Enter stop index : \n"))
step = int(input("Enter step : \n"))

for j in range(start, stop, step):
    print("hello_world ", j)
