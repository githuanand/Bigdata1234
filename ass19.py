import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -π to π
x_values = np.linspace(-np.pi, np.pi, 2000)

# Calculate corresponding y values using the sine function
y_values = np.sin(x_values)

# Create a new figure
plt.figure()

# Plot the sine wave
plt.plot(x_values, y_values, label=r"$y = \sin(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine Wave")
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
