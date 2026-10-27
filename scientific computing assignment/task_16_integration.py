
import numpy as np
from scipy.integrate import simpson

print("TASK 16: NUMERICAL INTEGRATION")

time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

# Original example: calculate energy consumption
trapezoid_energy = np.trapezoid(power_kw, x=time_hours)
simpson_energy = simpson(power_kw, x=time_hours)

print("\nOriginal example")
print("Trapezoidal energy:", trapezoid_energy, "kWh")
print("Simpson energy:", simpson_energy, "kWh")

# Modification: change the power readings
modified_power = power_kw * 1.2
modified_trapezoid = np.trapezoid(modified_power, x=time_hours)
modified_simpson = simpson(modified_power, x=time_hours)

print("\nModified example: power readings increased by 20%")
print("Trapezoidal energy:", modified_trapezoid, "kWh")
print("Simpson energy:", modified_simpson, "kWh")

# Related application: estimate solar energy production
solar_power_kw = np.array([0, 0.5, 1.5, 2.5, 2.0, 1.0, 0])
solar_energy = np.trapezoid(solar_power_kw, x=time_hours)

print("\nSolar application")
print("Estimated solar energy:", solar_energy, "kWh")
