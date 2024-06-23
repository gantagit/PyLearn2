# Functions Scope and Lifetime
# Function within another function

def outer_func():
    outer_func_a = 10

    def inner_func_1():
        print("adding 1 to the variable of outer function: ", outer_func_a + 1)

    inner_func_1()

    def inner_func_2():
        print("adding 2 to the variable of outer function: ", outer_func_a + 2)

    inner_func_2()

    print("variable of outer function: ", outer_func_a)


outer_func()
