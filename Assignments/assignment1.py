import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 400)  # Generate 400 points from -10 to 10

# Define the math functions you want to plot
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x ** 2

# Create a new figure and axis
plt.figure()

# Plot the functions
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='x^2')

# Add labels and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Math Functions')
plt.legend()

# Display the plot
plt.show()
