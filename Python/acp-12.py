class Shapes:
    def make_area(self):
        pass

class Square(Shapes):
    def make_area(self):
        print("SQUARE = 4 * SIDE")

class Rectangle(Shapes):
    def make_area(self):
        print("RECTANGLE = LENGTH * BREADTH")

class Triangle(Shapes):
    def make_area(self):
        print("TRIANGLE = 1/2 * BASE * HEIGHT")


def shapes_area(shape):
    shape.make_area()
triangle = Triangle()
square = Square()
rectangle = Rectangle()

shapes_area(triangle)
shapes_area(rectangle)
shapes_area(square)
