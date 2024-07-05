# Inheritance

# Multiple inheritance
# Multi parent Single Child

class Father:
    gold = "2kg"

    def father_method(self):
        print("This is father class")


class Mother:
    gold = "3kg"

    def mother_method(self):
        print("This is mother class")


class Child(Mother, Father):

    def child_method(self):
        print("This is child class")


ch = Child()
ch.mother_method()
ch.father_method()
ch.child_method()
print(ch.gold)  # Method 1
print(Child.gold)  # Method 2
print(Mother.gold)  # Method 3
print(Father.gold)  # Method 4
