class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        # Method to calculate the area of the rectangle
        return self.length * self.breadth

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle
        return 2 * (self.length + self.breadth)

    def compare_area(self, other):
        # Compare the area of two rectangles
        if self.area() > other.area():
            return "First rectangle has a larger area."
        elif self.area() < other.area():
            return "Second rectangle has a larger area."
        else:
            return "Both rectangles have the same area."

# Getting user input for two rectangles
print("Enter details for the first rectangle:")
length1 = float(input("Enter length: "))
breadth1 = float(input("Enter breadth: "))
rect1 = Rectangle(length1, breadth1)

print("\nEnter details for the second rectangle:")
length2 = float(input("Enter length: "))
breadth2 = float(input("Enter breadth: "))
rect2 = Rectangle(length2, breadth2)

# Displaying the area and perimeter of both rectangles
print(f"\nFirst Rectangle: Area = {rect1.area()}, Perimeter = {rect1.perimeter()}")
print(f"Second Rectangle: Area = {rect2.area()}, Perimeter = {rect2.perimeter()}")

# Comparing the areas of the two rectangles
print("\nComparison of Areas:")
print(rect1.compare_area(rect2))
