
import numpy as np
from scipy.optimize import root

print("TASK 12: SOLVING NONLINEAR EQUATIONS")


def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ]


# Original example: intersections of a circle and a parabola
for guess in ([1, 1], [-1, 1]):
    result = root(equations, guess)
    print("\nStarting guess:", guess)
    print("Solution:", np.round(result.x, 6))
    print("Converged:", result.success)
    print("Residuals:", np.round(equations(result.x), 8))

# Modification: use different starting guesses
for guess in ([1.5, 1.5], [-1.5, 1.5]):
    result = root(equations, guess)
    print("\nModified starting guess:", guess)
    print("Solution:", np.round(result.x, 6))
    print("Converged:", result.success)

# Related application: determine points where two design constraints meet
design_result = root(equations, [1, 1])
x, y = design_result.x
print("\nDesign intersection:")
print("x =", round(x, 6), "y =", round(y, 6))
print("Both equations are approximately satisfied:",
      np.linalg.norm(equations(design_result.x)) < 1e-6)
