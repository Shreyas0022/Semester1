def compare(S1, S2, n):
   
    if S1[:n] == S2[:n]:
        return True
    else:
        return False

S1 = input("Enter the String1:")
S2 = input("Enter the String2:")
n = int(input("Enter the number of characters to Compare: "))

result = compare(S1, S2, n)

if result:
    print(f"The first {n} characters of both the strings are Same.")
else:
    print(f"The first {n} characters of both the strings are not Same.")
