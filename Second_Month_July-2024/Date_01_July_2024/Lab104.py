# Inheritance

# Hybrid inheritance

class A:
    def methodA(self):
        print("A method")


class B(A):
    def methodB(self):
        print("B method")


class C(A):
    def methodC(self):
        print("C method")


class D(B, C):  # Multiple inheritance, Multi-level inheritance

    def methodD(self):
        print("D method")


d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
print("*************************")
