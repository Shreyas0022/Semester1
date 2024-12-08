def fibonacci(n):
        if n<=1:
                return n
        else:
                return fibonacci(n-1) + fibonacci(n-2)
number=int(input("Enter the number of terms:"))
if number<=0:
        print("Enter a positive number")
else:
        print("Fibonacci Series:")
        for i in range(number):
                print(fibonacci(i))
