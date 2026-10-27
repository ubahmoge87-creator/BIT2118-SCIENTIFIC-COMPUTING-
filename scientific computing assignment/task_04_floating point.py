
import numpy as np

print("TASK 4: FLOATING-POINT ERRORS AND NUMERICAL STABILITY")

# PART 1: ORIGINAL EXAMPLE - FLOATING-POINT COMPARISON

calculated = 0.1 + 0.2
expected = 0.3

print("\nPART 1: FLOATING-POINT COMPARISON")
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

# PART 2: ORIGINAL EXAMPLE - ABSOLUTE AND RELATIVE ERROR

true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nPART 2: ABSOLUTE AND RELATIVE ERROR")
print("True value:", true_value)
print("Approximate value:", approx_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# PART 3: MODIFICATION - USE A MORE ACCURATE APPROXIMATION

modified_approx_value = 1.4142

modified_absolute_error = abs(true_value - modified_approx_value)
modified_relative_error = modified_absolute_error / abs(true_value)

print("\nPART 3: MODIFIED APPROXIMATION")
print("Original approximation:", approx_value)
print("Improved approximation:", modified_approx_value)
print(f"Original absolute error: {absolute_error:.8f}")
print(f"Improved absolute error: {modified_absolute_error:.8f}")
print(f"Original relative error: {relative_error:.8%}")
print(f"Improved relative error: {modified_relative_error:.8%}")

# PART 4: ORIGINAL EXAMPLE - NUMERICAL STABILITY

print("\nPART 4: NUMERICAL STABILITY")

for x in [1e-4, 1e-8, 1e-12]:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)

    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

# PART 5: RELATED REAL-WORLD APPLICATION - TEMPERATURE SENSOR

reference_temperature = 25.0
measured_temperature = 24.98
allowed_error = 0.05

sensor_absolute_error = abs(
    reference_temperature - measured_temperature
)

sensor_relative_error = (
    sensor_absolute_error / abs(reference_temperature)
)

sensor_acceptable = np.isclose(
    measured_temperature,
    reference_temperature,
    atol=allowed_error,
    rtol=0
)

print("\nPART 5: TEMPERATURE SENSOR CALIBRATION")
print("Reference temperature:", reference_temperature, "degrees C")
print("Measured temperature:", measured_temperature, "degrees C")
print(f"Absolute error: {sensor_absolute_error:.4f} degrees C")
print(f"Relative error: {sensor_relative_error:.4%}")
print("Within allowed tolerance:", sensor_acceptable)

if sensor_acceptable:
    print("Result: The sensor reading is acceptable.")
else:
    print("Result: The sensor reading is outside the allowed tolerance.")
