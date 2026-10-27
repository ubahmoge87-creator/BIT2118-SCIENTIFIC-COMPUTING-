
import numpy as np

print("TASK 8: JACOBI AND GAUSS-SEIDEL METHODS")

A = np.array([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, 0, 0],
    [0, -1, 2, -1, 0],
    [0, 0, -1, 2, -1],
    [0, 0, 0, -1, 2]
], dtype=float)

b = np.array([100, 0, 0, 0, 20], dtype=float)

# Original example: direct solution
direct = np.linalg.solve(A, b)
print("\nDirect solution:", np.round(direct, 4))


def jacobi(A, b, tolerance=1e-8, max_iterations=10000):
    x = np.zeros_like(b, dtype=float)
    for _ in range(max_iterations):
        new_x = (b - (A @ x - np.diag(A) * x)) / np.diag(A)
        if np.linalg.norm(new_x - x, ord=np.inf) < tolerance:
            return new_x
        x = new_x
    return x


def gauss_seidel(A, b, tolerance=1e-8, max_iterations=10000):
    x = np.zeros_like(b, dtype=float)
    for _ in range(max_iterations):
        old_x = x.copy()
        for i in range(len(b)):
            left = A[i, :i] @ x[:i]
            right = A[i, i+1:] @ old_x[i+1:]
            x[i] = (b[i] - left - right) / A[i, i]
        if np.linalg.norm(x - old_x, ord=np.inf) < tolerance:
            return x
    return x


# Original iterative methods
j_solution = jacobi(A, b)
gs_solution = gauss_seidel(A, b)

print("Jacobi solution:", np.round(j_solution, 4))
print("Gauss-Seidel solution:", np.round(gs_solution, 4))

# Modification: change the boundary values
modified_b = np.array([80, 0, 0, 0, 30], dtype=float)
print("\nModified boundary values:", modified_b)
print("Modified Jacobi solution:", np.round(jacobi(A, modified_b), 4))
print("Modified Gauss-Seidel solution:",
      np.round(gauss_seidel(A, modified_b), 4))

# Related application: temperature distribution in a five-point rod model
rod_b = np.array([60, 0, 0, 0, 10], dtype=float)
rod_temperature = gauss_seidel(A, rod_b)
print("\nRod temperature model values:", np.round(rod_temperature, 4))
print("Residual:", np.round(A @ rod_temperature - rod_b, 8))
