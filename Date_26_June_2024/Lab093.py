class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def modulo(self):
        return self.a % self.b

    def floor_div(self):
        return self.a // self.b

    def power(self):
        return self.a ** self.b


def perform_operation(operation1, a, b):
    calc = Calc(a, b)
    operations = {
        1: calc.add,
        2: calc.minus,
        3: calc.multiply,
        4: calc.divide,
        5: calc.modulo,
        6: calc.floor_div,
        7: calc.power
    }

    if operation1 in operations:
        result = operations[operation]()
        print(result)
    else:
        print("Invalid Input")


nums1 = float(input("Enter first number: "))
nums2 = float(input("Enter second number: "))
operation = int(input("Enter"
                      "\n1 for Addition"
                      "\n2 for Subtraction"
                      "\n3 for Multiplication"
                      "\n4 for Division"
                      "\n5 for Modulo"
                      "\n6 for Floor Division"
                      "\n7 for Power\n"))

perform_operation(operation, nums1, nums2)
