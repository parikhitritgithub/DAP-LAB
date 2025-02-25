import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)  # Set of all lowercase letters
    s = s.lower()  # Convert input to lowercase
    s = set(s)  # Convert string to a set of characters
    return alphabet.issubset(s)  # Check if all letters are present

# Taking user input
sentence = input("Enter a sentence: ")

if is_pangram(sentence):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

