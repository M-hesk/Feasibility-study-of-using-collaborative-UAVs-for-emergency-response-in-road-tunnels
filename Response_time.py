import numpy as np
import matplotlib.pyplot as plt

# Set the distance to travel (in meters)
distance = 2000

# Set the minimum and maximum speeds (in meters per minute)
min_speed = 200
max_speed = 1500

# Generate an array of speeds (in meters per minute)
speeds1 = np.linspace(min_speed, max_speed, 100)

# Calculate the time it takes to travel the distance at each speed
times1 = distance / speeds1

# Plot the times as a function of the speeds
plt.plot(speeds1, times1)

plt.axvline(x=360, color='red', linestyle=":", label="Mini3")
plt.axvline(x=540, color='blue', linestyle="--", label="Mavic3")
plt.axvline(x=600, color='green', linestyle="-",  label="Autel Lite+")
plt.axvline(x=617, color='purple', linestyle="-.", label="Autel Evo Pro")
plt.axvline(x=600, color='orange', linestyle="--", marker='o', label="Air2S")
x_coord1 = 360
x_coord2 = 540
x_coord3 = 617
x_coord4 = 600
y_coord1 = np.interp(x_coord1, speeds1, times1)
y_coord2 = np.interp(x_coord2, speeds1, times1)
y_coord3 = np.interp(x_coord3, speeds1, times1)
y_coord4 = np.interp(x_coord4, speeds1, times1)
# Print the corresponding y-coordinate
print("The time it takes to travel {} meters at {} m/min is {:.2f} minutes".format(distance, x_coord1, y_coord1))
print("The time it takes to travel {} meters at {} m/min is {:.2f} minutes".format(distance, x_coord2, y_coord2))
print("The time it takes to travel {} meters at {} m/min is {:.2f} minutes".format(distance, x_coord3, y_coord3))
print("The time it takes to travel {} meters at {} m/min is {:.2f} minutes".format(distance, x_coord4, y_coord4))



plt.plot(x_coord1, y_coord1, marker='o', color='black')
plt.plot(x_coord2, y_coord2, marker='o', color='black')
plt.plot(x_coord3, y_coord3, marker='o', color='black')
plt.xlabel('Speed (meters per minute)')
plt.ylabel('Time (minutes)')
plt.legend()
plt.title('Time to travel {} meters'.format(distance))
plt.savefig('C:/Users/mariu/BachelorOppgave\ResponseTimePlotAvg', dpi=500)
plt.show()