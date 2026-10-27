
import numpy as np


# TASK 2: NUMPY ARRAYS AND NUMERICAL COMPUTATION
# # This program:
# 1. Analyses the original weather station temperatures.
# 2. Modifies the input to represent a greenhouse.
# 3. Applies the same calculations to a food-storage facility.
# PART 1: ORIGINAL EXAMPLE - WEATHER STATION


# Input: 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Calculate the mean, minimum and maximum
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Convert Celsius to Fahrenheit: F = 1.8C + 32
temperatures_f = 1.8 * temperatures_c + 32

print("PART 1: ORIGINAL WEATHER STATION")
print(f"Mean temperature: {mean_temp:.2f} °C")
print(f"Minimum temperature: {min_temp:.2f} °C")
print(f"Maximum temperature: {max_temp:.2f} °C")
print("First six Fahrenheit readings:", temperatures_f[:6])

# PART 2: MODIFICATION - GREENHOUSE MONITORING


# Modification: Change the input from 24 weather readings
# to six illustrative greenhouse temperature readings.
greenhouse_temps_c = np.array([
    22.0, 24.0, 25.0, 27.0, 26.0, 29.0
])

# Apply the same calculations to the modified input
greenhouse_mean = np.mean(greenhouse_temps_c)
greenhouse_min = np.min(greenhouse_temps_c)
greenhouse_max = np.max(greenhouse_temps_c)

greenhouse_temps_f = 1.8 * greenhouse_temps_c + 32

print("\nPART 2: MODIFIED GREENHOUSE")
print(f"Mean temperature: {greenhouse_mean:.2f} °C")
print(f"Minimum temperature: {greenhouse_min:.2f} °C")
print(f"Maximum temperature: {greenhouse_max:.2f} °C")
print("Fahrenheit readings:", greenhouse_temps_f)


# PART 3: DIFFERENT RELATED APPLICATION - FOOD STORAGE
# New application: Monitor temperatures in a food-storage
# facility using six illustrative sensor readings.
storage_temps_c = np.array([
    3.5, 4.0, 4.2, 5.0, 3.8, 4.5
])

# Calculate temperature statistics
storage_mean = np.mean(storage_temps_c)
storage_min = np.min(storage_temps_c)
storage_max = np.max(storage_temps_c)

# Convert the readings to Fahrenheit
storage_temps_f = 1.8 * storage_temps_c + 32

print("\nPART 3: FOOD-STORAGE MONITORING")
print(f"Mean temperature: {storage_mean:.2f} °C")
print(f"Minimum temperature: {storage_min:.2f} °C")
print(f"Maximum temperature: {storage_max:.2f} °C")
print("Fahrenheit readings:", storage_temps_f)

# Example threshold check for demonstration
# The 5°C threshold is an illustrative assumption.
threshold = 5.0

if storage_max > threshold:
    print("Warning: A reading exceeded the example threshold.")
else:
    print("No reading exceeded the example threshold.")
