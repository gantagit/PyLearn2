# Inheritance

# single inheritance
class Grandparent:
    key = "All@123"

    def grand_parent_method(self):
        return "This is grand parent method in grand parent class"


class Parent(Grandparent):  # here we are inheriting the Grandparent class

    def parent_method(self):
        return "This is parent method in parent class"


parent = Parent()
print(parent.key)
print(parent.grand_parent_method())
print(parent.parent_method())
