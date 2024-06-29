import matplotlib.pyplot as plt
import numpy as np

def draw_straight_line(slope, x_min, x_max):
    # Generate x values within the specified range
    x_values = np.linspace(x_min, x_max, 100)
    
    # Calculate corresponding y values using the slope
    y_values = slope * x_values
    
    # Create a new figure
    plt.figure()
    
    # Plot the line
    plt.plot(x_values, y_values, label=f"y = {slope}x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Straight Line")
    plt.grid(True)
    plt.legend()
    
    # Display the plot
    plt.show()

# Example usage
slope_value = float(input("Enter the slope value: "))
x_min_value = float(input("Enter the minimum x value: "))
x_max_value = float(input("Enter the maximum x value: "))

draw_straight_line(slope_value, x_min_value, x_max_value)



#output:-

#Enter the slope value: 1
#Enter the minimum x value: 0.5
#Enter the maximum x value: 3
