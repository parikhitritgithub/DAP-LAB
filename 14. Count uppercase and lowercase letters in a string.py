s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
