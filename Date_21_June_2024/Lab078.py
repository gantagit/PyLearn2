# Dictionaries

# Two ways we can create dictionaries
my_dict = {"name": "Vijay", "age": "45"}  # first way to define dictionary
print(my_dict)

my_dict_1 = dict(name="Ganta", age=20)  # second way of defining the dictionary
print(my_dict_1)
my_dict_1 = dict([("name", "Ganta"), ("age", 20)])  # third way of defining the dictionary

print(my_dict_1.get("name"))
