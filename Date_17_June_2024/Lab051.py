# functions  with *args # here *args means we can pass any number of arguments to the function
def print_all(*args):
    print(args)


print_all(1, 2, 3, "Vijay", 3.14)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
def print_args(*args):
    for i in args:
        print(i, end="\t")


print_args(1, 2, 3, "Vijay", 3.14, "\n")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
a = ["Vijay", 1, 2, 3, 3.14, -1, "Ganta"]
for i in a:
    print(i, end="\n")
