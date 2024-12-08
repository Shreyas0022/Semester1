square = lambda side: side * side
rectangle = lambda length, width: length * width
triangle = lambda base, height: 0.5 * base * height

while True:
    print("\n2D SHAPES")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    
    choice = input("\nSelect any Shape to calculate its Area :: ")

    if choice == '1':
        side = float(input("\nEnter the side length of the square: "))
        print(f" The Area of the Square is: {square(side)}")

    elif choice == '2':
        length = float(input("\nEnter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f" The Area of the Rectangle is: {rectangle(length, width)}")

    elif choice == '3':
        base = float(input("\nEnter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f" The Area of the Triangle is: {triangle(base, height)}")

    elif choice == '4':
        print("Exiting")
        break

    else:
        print("Invalid choice!")
