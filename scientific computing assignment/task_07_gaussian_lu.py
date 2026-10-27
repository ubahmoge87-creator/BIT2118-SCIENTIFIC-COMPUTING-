
import numpy as np
from scipy.linalg import lu_factor, lu_solve

print("TASK 7: LU DECOMPOSITION")

A = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 3]
], dtype=float)

b = np.array([15, 10, 10], dtype=float)

# Original example: solve the linear system
solution = np.linalg.solve(A, b)
print("\nOriginal solution:", solution)
print("Original residual:", A @ solution - b)

# Modification: change the measurements
modified_b = np.array([16, 11, 9], dtype=float)
lu, piv = lu_factor(A)
modified_solution = lu_solve((lu, piv), modified_b)

print("\nModified measurements:", modified_b)
print("Modified solution:", modified_solution)
print("Modified residual:", A @ modified_solution - modified_b)

# Related application: estimate equipment settings for three connected zones
zone_readings = np.array([14, 12, 11], dtype=float)
zone_solution = lu_solve((lu, piv), zone_readings)

print("\nRelated application: connected-zone system")
print("Estimated zone values:", zone_solution)
print("Residual:", A @ zone_solution - zone_readings)
