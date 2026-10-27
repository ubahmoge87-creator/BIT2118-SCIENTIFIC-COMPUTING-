
import numpy as np
from scipy.optimize import minimize

print("TASK 19: NUMERICAL OPTIMIZATION")

cost_A = 12
cost_B = 18
capacity_A = 100
capacity_B = 170
required_capacity = 1000


def total_cost(servers):
    x, y = servers
    return cost_A * x + cost_B * y


def capacity_constraint(servers):
    x, y = servers
    return capacity_A * x + capacity_B * y - required_capacity


# Original example: minimize cost subject to capacity
result = minimize(
    total_cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints=[{"type": "ineq", "fun": capacity_constraint}]
)

print("\nOriginal optimization")
print("Optimization successful:", result.success)
print("Type A servers:", result.x[0])
print("Type B servers:", result.x[1])
print("Total capacity:", capacity_A * result.x[0] + capacity_B * result.x[1])
print("Total cost:", result.fun)

# Modification: increase required capacity
modified_requirement = 1500

modified_result = minimize(
    total_cost,
    x0=[8, 5],
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints=[{
        "type": "ineq",
        "fun": lambda s: capacity_A * s[0] + capacity_B * s[1]
        - modified_requirement
    }]
)

print("\nModified required capacity:", modified_requirement)
print("Type A servers:", modified_result.x[0])
print("Type B servers:", modified_result.x[1])
print("Total cost:", modified_result.fun)

# Related application: compare whole-server combinations
candidates = []
for x in range(0, 20):
    for y in range(0, 20):
        capacity = capacity_A * x + capacity_B * y
        if capacity >= required_capacity:
            candidates.append((cost_A*x + cost_B*y, x, y, capacity))

best = min(candidates)

print("\nWhole-server application")
print("Type A servers:", best[1])
print("Type B servers:", best[2])
print("Capacity:", best[3])
print("Cost:", best[0])
