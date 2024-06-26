# Decorators
# What is Decorator?
# Decorator is a function that takes another function as an argument and extends its functionality.

# Example 1: Adding a new functionality to a function

def my_deco(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_deco
def hello():
    print("Hello World")


hello()

