number = list(map(int,input("Enter the numbers : ").split(",")))

power = list(map(lambda x: 2 ** x, number))

print(f" The Powers of 2 for the Entered Numbers: {power}")

