class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    add = lambda self: self.a + self.b
    minus = lambda self: self.a - self.b
    multiply = lambda self: self.a * self.b
    divide = lambda self: self.a / self.b
    modulo = lambda self: self.a % self.b

    def floor_div(self):
        return self.a // self.b

    def power(self):
        return self.a ** self.b

    # def perform_operation(self):
    #     match self.perform:
    #         case 1:
    #             return Calc.add(self.a, self.b)
    #         case _:
    #             print("Invalid Input")

# def perform_operation(perform):
#     match perform:
#         case 1:
#             return Calc.add(self)
#         case 2:
#             return Calc.minus()
#         case 3:
#             print(cal.multiply())
#         case 4:
#             print(cal.divide())
#         case 5:
#             print(cal.modulo())
#         case 6:
#             print(cal.floor_div())
#         case 7:
#             print(cal.power())
#         case _:
#             print("Invalid Input")
