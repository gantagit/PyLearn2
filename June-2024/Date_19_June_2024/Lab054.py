# Functions Scope and Lifetime
# global variables and local variables

global_a = 10


def func_scope():
    local_a = 20
    print("local_a ", local_a)
    print("global_a ", global_a - 1)
    print("global_a ", global_a - 1)


# print(local_a)
func_scope()
print("global_a ", global_a + 2)
