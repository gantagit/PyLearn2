# Inheritance

# single inheritance
class Parent:
    key = "123456"

    def parent_method(self):
        print("This is parent class")


class Child(Parent):

    def child_method(self):
        print("This is child class")


ch = Child()
ch.child_method()
ch.parent_method()
print(ch.key)  # accessing parent class variable
