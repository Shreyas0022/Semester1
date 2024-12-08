def add(x,y):
        return x + y
def subtract(x,y):
        return x - y
def multiply(x,y):
        return x * y
def divide(x,y):
        if y==0:
                return "Error! Division by Zero"
        return x/y
while  True:
        print("\n1.ADDITION")
        print("2.SUBTRACTION")
        print("3.MULTIPLICATION")
        print("4.DIVISION")
        print("5.EXIT\n")
        choice = input("   Select an Operation::")
        if choice=='5':
                print("Exiting")
                break
        if choice in ('1','2','3','4'):
                num1=float(input("Enter the First Number:"))
                num2=float(input("Enter the Second Number:"))

                if choice == '1':
                        print(f"\nResult: {num1} + {num2} = {add(num1,num2)}")
                elif choice == '2':
                        print(f"\nResult: {num1} - {num2} = {subtract(num1,num2)}")
                elif choice == '3':
                        print(f"\nResult: {num1} * {num2} = {multiply(num1,num2)}")
                elif choice == '4':
                        print(f"\nResult: {num1} / {num2} = {divide(num1,num2)}")
        else:
                print("Invalid Choice")
