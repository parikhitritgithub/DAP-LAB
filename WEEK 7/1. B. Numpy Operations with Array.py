import numpy as np

# Define the two arrays
a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 2], [4, 5]])

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Dot product")
    print("6. Exponentiation")
    print("7. Logarithm (base e)")
    print("8. Logarithm (base 10)")
    print("9. Exit")

    try:
        n = int(input("Enter the option number: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if n == 1:
        c = np.add(a, b)
        print("Sum:\n", c, "\n")
    elif n == 2:
        d = np.subtract(a, b)
        print("Difference:\n", d, "\n")
    elif n == 3:
        e = np.multiply(a, b)
        print("Product:\n", e, "\n")
    elif n == 4:
        f = np.divide(a, b)
        print("Quotient:\n", f, "\n")
    elif n == 5:
        g = np.dot(a, b)
        print("Dot Product:\n", g, "\n")
    elif n == 6:
        h = np.exp(a)
        i = np.exp(b)
        print("Exponentiation for array a:\n", h)
        print("Exponentiation for array b:\n", i, "\n")
    elif n == 7:
        l = np.log(a)
        m = np.log(b)
        print("Natural Logarithm (ln) for array a:\n", l)
        print("Natural Logarithm (ln) for array b:\n", m, "\n")
    elif n == 8:
        x = np.log10(a)
        y = np.log10(b)
        print("Logarithm (base 10) for array a:\n", x)
        print("Logarithm (base 10) for array b:\n", y, "\n")
    elif n == 9:
        print("Exiting the program.")
        break
    else:
        print("No such option exists, please enter an existing option.\n")
