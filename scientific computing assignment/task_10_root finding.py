
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

print("TASK 10: ROOT FINDING")


def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)


def fixed_point(T):
    return 25 + 10 * np.exp(-T / 20)


# Original example: bisection method
result = root_scalar(heat_balance, bracket=[
                     20, 40], method="bisect", xtol=1e-10)
root = result.root
print("\nOriginal root:", root)
print("Function at root:", heat_balance(root))

# Original example: fixed-point iteration
T = 30.0
for iteration in range(1000):
    new_T = fixed_point(T)
    if abs(new_T - T) < 1e-10:
        T = new_T
        break
    T = new_T

print("Fixed-point root:", T)
print("Iterations:", iteration + 1)

# Modification: change the heat input from 10 to 15


def modified_balance(T):
    return T - 25 - 15 * np.exp(-T / 20)


modified_result = root_scalar(
    modified_balance, bracket=[20, 45], method="bisect"
)
print("\nModified heat-input root:", modified_result.root)

# Related application: estimate a temperature equilibrium
temperatures = np.linspace(20, 45, 300)
plt.plot(temperatures, [heat_balance(t)
         for t in temperatures], label="Original")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(root, linestyle="--", label=f"Root = {root:.2f}")
plt.xlabel("Temperature")
plt.ylabel("Heat-balance function")
plt.title("Finding a Heat-Balance Root")
plt.legend()
plt.grid(True)
plt.show()
