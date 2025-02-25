numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = 1

for num in numbers:
    result *= num

print("Product of numbers:", result)
