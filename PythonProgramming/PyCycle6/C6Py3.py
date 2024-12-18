from abc import ABC, abstractmethod

# Abstract class Polygon
class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Derived class Rectangle from Polygon
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        # Area of a rectangle = length * width
        area = self.length * self.width
        return area

# Derived class Triangle from Polygon
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        # Area of a triangle = 0.5 * base * height
        area = 0.5 * self.base * self.height
        return area

# Getting user input for rectangle
print("Enter dimensions for Rectangle:")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
print(f"Area of Rectangle: {rectangle_area}")

# Getting user input for triangle
print("\nEnter dimensions for Triangle:")
base = float(input("Enter base: "))
height = float(input("Enter height: "))
triangle = Triangle(base, height)
triangle_area = triangle.calculate_area()
print(f"Area of Triangle: {triangle_area}")
