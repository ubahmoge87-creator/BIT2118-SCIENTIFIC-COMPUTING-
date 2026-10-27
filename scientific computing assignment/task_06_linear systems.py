
import numpy as np

print("TASK 6: SOLVING LINEAR SYSTEMS")

# PART 1: ORIGINAL EXAMPLE - SERVER RESOURCE ALLOCATION

# Type A servers use 4 CPU units and 8 GB of memory.
# Type B servers use 2 CPU units and 12 GB of memory.
# The available resources are 20 CPU units and 72 GB of memory.

A = np.array([
    [4, 2],
    [8, 12]
], dtype=float)

b = np.array([20, 72], dtype=float)

solution = np.linalg.solve(A, b)

x = solution[0]
y = solution[1]

print("\nPART 1: ORIGINAL SERVER RESOURCE PROBLEM")
print("Coefficient matrix A:")
print(A)

print("Resource vector b:")
print(b)

print(f"Number of Type A servers: {x:.2f}")
print(f"Number of Type B servers: {y:.2f}")

print("CPU resources used:", 4*x + 2*y)
print("Memory used:", 8*x + 12*y, "GB")

residual = A @ solution - b
print("Residual:", residual)

# PART 2: MODIFICATION - CHANGE THE AVAILABLE RESOURCES

modified_b = np.array([28, 96], dtype=float)

modified_solution = np.linalg.solve(A, modified_b)

modified_x = modified_solution[0]
modified_y = modified_solution[1]

print("\nPART 2: MODIFIED SERVER RESOURCE PROBLEM")
print("Modified CPU resources:", modified_b[0])
print("Modified memory:", modified_b[1], "GB")

print(f"Number of Type A servers: {modified_x:.2f}")
print(f"Number of Type B servers: {modified_y:.2f}")

print("CPU resources used:", 4*modified_x + 2*modified_y)
print("Memory used:", 8*modified_x + 12*modified_y, "GB")

modified_residual = A @ modified_solution - modified_b
print("Residual:", modified_residual)

# PART 3: RELATED REAL-WORLD APPLICATION - FACTORY PRODUCTION

# Product A requires 2 machine-hours and 1 labour-hour.
# Product B requires 1 machine-hour and 3 labour-hours.
# The factory has 11 machine-hours and 13 labour-hours available.

factory_A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

factory_b = np.array([11, 13], dtype=float)

production = np.linalg.solve(factory_A, factory_b)

product_A = production[0]
product_B = production[1]

print("\nPART 3: FACTORY PRODUCTION APPLICATION")
print(f"Quantity of Product A: {product_A:.2f}")
print(f"Quantity of Product B: {product_B:.2f}")

print("Machine-hours used:", 2*product_A + product_B)
print("Labour-hours used:", product_A + 3*product_B)

factory_residual = factory_A @ production - factory_b
print("Residual:", factory_residual)

print("\nInterpretation:")
print("The solution gives the quantities that satisfy both resource equations.")
print("In practice, whole-product requirements may require integer quantities.")
