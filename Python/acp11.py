class Shape:
    def __init__(self, name="Generic Shape"):
        self.name = name

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement calculate_perimeter method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


rectangle = Rectangle(5, 10)
print(f"{rectangle.name} Area: {rectangle.calculate_area()}")
print(f"{rectangle.name} Perimeter: {rectangle.calculate_perimeter()}")

square = Square(7)
print(f"{square.name} Area: {square.calculate_area()}")
print(f"{square.name} Perimeter: {square.calculate_perimeter()}")