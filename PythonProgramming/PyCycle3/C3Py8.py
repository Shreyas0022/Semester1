limit1 = int(input("Enter the starting range:"))

limit2 = int(input("Enter the Ending range:"))
for num in range(limit1, limit2+1):
        digit_sum = 0
        for digit in str(num):
                digit_sum+=int(digit)
        if digit_sum > 1:
                prime=True
                for i in range(2, int(digit_sum ** 0.5) + 1):
                        if digit_sum % i == 0:
                                prime = False
                                break
                if prime:
                        print(f"Number = {num} ; Sum of Digits = {digit_sum}")

