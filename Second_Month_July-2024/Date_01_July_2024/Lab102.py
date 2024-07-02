# Inheritance

# Hierarchical inheritance
# Single parent Multi Child

class Father:
    gold = "2kg"

    def father_method(self):
        print("This is father class")


class Child1(Father):
    def child1_method(self):
        print("This is child1 class")


class Child2(Father):

    def child2_method(self):
        print("This is child2 class")


class Child3(Father):

    def child3_method(self):
        print("This is child3 class")


ch3 = Child3()
ch3.child3_method()
ch3.father_method()
print(ch3.gold)

ch2 = Child2()
ch2.child2_method()
