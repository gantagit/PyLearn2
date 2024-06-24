# list Functions Scope and Lifetime

list_1 = [1, 2, 3, 4]
double_list = []
# ++++++++++++++++++++++Double each item of the list using For loop ++++++++++++++++++++
for i in list_1:
    double_list.append(i * 2)
    # print(double_list)
print("double the list using for loop \n", double_list)

# ++++++++++++++++++++++Double each item using lambda++++++++++++++++++++
doubles_item = lambda num: num * 2
print("lambda for double an item ", doubles_item(10))

# +++++++++++++++++++++Double each item of the list using lambda and map++++++++++++++++++++++++++++++++++++

# Map(0
# 1. Takes Each item from the list
# 2. Execute the function on it
# 3. Return same number of elements (list)
# 4. Applies the lambda function to each item
# 3. Returns a map object
# 4. The list() function converts the map object to a list

list_1.append(5)

double_list_1 = list(map(doubles_item, list_1))
print("This is double list using lambda & map \n", double_list_1)
