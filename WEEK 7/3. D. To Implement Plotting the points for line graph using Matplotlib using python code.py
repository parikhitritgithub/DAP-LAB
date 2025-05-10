import matplotlib.pyplot as plt

# Data for line A
x1 = [1, 4, 6, 8]
y1 = [2, 5, 8, 9]
plt.plot(x1, y1, label="Line A", color="r")

# Data for line B
x2 = [3, 6, 8, 10]
y2 = [2, 4, 8, 9]
plt.plot(x2, y2, label="Line B", color="g")

# Setting axis limits
plt.xlim(0, 12)
plt.ylim(0, 12)

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")

# Showing legend
plt.legend()

# Display the plot
plt.show()
