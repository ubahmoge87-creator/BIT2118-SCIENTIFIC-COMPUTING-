
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

print("TASK 13: INTERPOLATION")

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperatures = np.array([18, 20, 22.5, 24, 25, 25.5, 25], dtype=float)

# Original example: linear and cubic interpolation
linear = interp1d(hours, temperatures, kind="linear")
cubic = CubicSpline(hours, temperatures)

print("\nOriginal estimate at 10:30:")
print("Linear:", float(linear(10.5)))
print("Cubic:", float(cubic(10.5)))

# Modification: estimate at 11:30 instead
print("\nModified estimate at 11:30:")
print("Linear:", float(linear(11.5)))
print("Cubic:", float(cubic(11.5)))

# Related application: estimate a missing hourly sensor reading
missing_hour = 12.5
print("\nEstimated sensor reading at 12:30:")
print("Linear:", float(linear(missing_hour)))
print("Cubic:", float(cubic(missing_hour)))

fine_hours = np.linspace(hours.min(), hours.max(), 200)
plt.plot(hours, temperatures, "o", label="Observed readings")
plt.plot(fine_hours, linear(fine_hours), label="Linear interpolation")
plt.plot(fine_hours, cubic(fine_hours), label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Temperature (degrees C)")
plt.title("Temperature Interpolation")
plt.legend()
plt.grid(True)
plt.show()
