# function example for NO RETURN AND NO ARGUMENTS
def my_name():
    print("My name is Vijay")


my_name()  # Calling the function


# +++++++++++++++++++++++++++++++++++++++++++++
# function example for NO RETURN WITH ARGUMENTS
def my_name_2(name):
    print("My name is ", name)


my_name_2("Vijay")  # Calling the function with argument


def my_name_3(name="Vijay"):
    print("My name is ", name)


my_name_3()  # Calling the function without argument
my_name_3("Ganta")  # Calling the function with argument
my_name_3(name="Pramod")  # Calling the function with argument


# +++++++++++++++++++++++++++++++++++++++++++++
# function example for RETURN WITH NO ARGUMENTS

def my_name_4():
    return True


result = my_name_4()
print(result)


# +++++++++++++++++++++++++++++++++++++++++++++
# function example for RETURN WITH ARGUMENTS

def my_name_5(name):
    return name


print(my_name_5("Vijay"))
