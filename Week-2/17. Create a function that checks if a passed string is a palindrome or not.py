def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]  

# Taking user input
string = input("Enter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
