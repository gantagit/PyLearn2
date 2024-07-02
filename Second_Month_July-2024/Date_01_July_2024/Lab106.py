# Polymorphism

class Shape:

    def __init__(self):
        pass

    def area(self):
        print("This is area of a shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of a circle is", 3.14 * self.radius ** 2)


class Rect(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # def area(self):
        # print("Area of a rectangle is", self.length * self.breadth)



area_circle = Circle(5)
area_circle.area()
area_rect = Rect(3, 4)
area_rect.area()
area_shape = Shape()
area_shape.area()
