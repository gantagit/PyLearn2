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
