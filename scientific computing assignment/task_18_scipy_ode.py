
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

print("TASK 18: SOLVING AN ODE WITH SCIPY")

voltage_supply = 5.0
resistance = 1000.0
capacitance = 0.001
initial_voltage = 0.0


def capacitor_ode(t, y):
    voltage = y[0]
    return [(voltage_supply - voltage) / (resistance * capacitance)]


time_points = np.linspace(0, 5, 200)

# Original example: solve capacitor charging equation
result = solve_ivp(
    capacitor_ode,
    [0, 5],
    [initial_voltage],
    t_eval=time_points
)

exact_voltage = voltage_supply * (
    1 - np.exp(-time_points / (resistance * capacitance))
)

print("\nOriginal example")
print("Solver successful:", result.success)
print("Voltage at 5 seconds:", result.y[0, -1], "V")
print("Maximum absolute error:", np.max(np.abs(result.y[0] - exact_voltage)))

# Modification: change the capacitance
modified_capacitance = 0.002


def modified_ode(t, y):
    return [(voltage_supply - y[0]) / (resistance * modified_capacitance)]


modified = solve_ivp(
    modified_ode, [0, 5], [initial_voltage], t_eval=time_points
)

print("\nModified capacitance:", modified_capacitance, "F")
print("Voltage at 5 seconds:", modified.y[0, -1], "V")

# Related application: simulate charging a capacitor in an electronic circuit
plt.plot(time_points, result.y[0], label="Original capacitance")
plt.plot(time_points, modified.y[0], label="Modified capacitance")
plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.show()
