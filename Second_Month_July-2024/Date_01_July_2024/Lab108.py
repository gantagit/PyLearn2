# Polymorphism

class Sums:

    def sum_of_variables(self, a=0, b=0, c=0):
        print("Sum of variables", a + b + c)

    def sum_of_variables(self, a, b):
        print("Sum of variables", a + b)


s = Sums()
s.sum_of_variables(a=2, b=3, c=4)
s.sum_of_variables(5, 6)
# operation1 = s.sum_of_variables(a=2, b=3, c=4)
# operation2 = s.sum_of_variables(5, 6)
# print(operation1)
# print(operation2)
