# Polymorphism
# Python doesn't support method overloading in traditional sense.
# super()

class Parent:

    # def __init__(self, name):
    #     print('Parent __init__', name)

    def home(self):
        print("This is parent home")


class Child(Parent):
    # def __init__(self, name):
    #     self.name = name

    def home(self):  # this is method overriding
        # super().home()
        print("This is child home")


child = Child()
child.home()
