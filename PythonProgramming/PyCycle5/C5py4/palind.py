def is_palindrome(s):
 s = s.lower()
 return s==s[::-1]

def palindrome_length(s):
 n=len(s)
 if n==0:
     return s
 longest=""
 

 for i in range(n):
  for j in range(i+1,n+1):
   substr=s[i:j]
   if is_palindrome(substr) and len(substr)>len(longest):
    longest=substr
 return longest
