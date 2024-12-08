import palind as p


s= input(" Enter the String: ")

if p.is_palindrome(s):
    print(f"{s} is Palindromic")
else:
 print(f"{s} is not palindromic")
 print(f"Longest palindromic substring in {s} is \n{p.palindrome_length(s)}")
