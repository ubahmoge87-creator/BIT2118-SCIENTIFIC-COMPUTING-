
import numpy as np
import matplotlib.pyplot as plt

print("TASK 15: NUMERICAL DIFFERENTIATION")

time = np.linspace(0, 10, 101)

# Original example: position of a moving object
position = 3 * time**2 + 2 * time

velocity = np.gradient(position, time)
acceleration = np.gradient(velocity, time)

print("\nOriginal example")
print("Position at 5 seconds:", position[50])
print("Estimated velocity at 5 seconds:", velocity[50])
print("Estimated acceleration at 5 seconds:", acceleration[50])

# Modification: change the position equation
modified_position = 2 * time**2 + 4 * time
modified_velocity = np.gradient(modified_position, time)
modified_acceleration = np.gradient(modified_velocity, time)

print("\nModified example")
print("Position at 5 seconds:", modified_position[50])
print("Estimated velocity at 5 seconds:", modified_velocity[50])
print("Estimated acceleration at 5 seconds:", modified_acceleration[50])

# Related application: estimate speed from vehicle position readings
vehicle_position = 5 * time + 0.5 * time**2
vehicle_speed = np.gradient(vehicle_position, time)

print("\nVehicle application")
print("Estimated speed at 5 seconds:", vehicle_speed[50], "m/s")

plt.plot(time, position, label="Position")
plt.plot(time, velocity, label="Velocity")
plt.plot(time, acceleration, label="Acceleration")
plt.xlabel("Time (seconds)")
plt.title("Numerical Differentiation")
plt.legend()
plt.grid(True)
plt.show()
