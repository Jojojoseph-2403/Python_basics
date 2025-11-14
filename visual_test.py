import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot
plt.plot(x, y)
plt.title("Simple Sine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

# Save image
plt.savefig("sine_plot.png")

print("Plot created successfully!")

