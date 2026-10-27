
import numpy as np
import matplotlib.pyplot as plt

print("TASK 20: MONTE CARLO SIMULATION")

rng = np.random.default_rng(42)

capacity = 1000
mean_demand = 850
standard_deviation = 120
number_of_simulations = 100_000

# Original example: simulate server demand
demand = rng.normal(
    mean_demand,
    standard_deviation,
    number_of_simulations
)

overloads = demand > capacity
overload_count = np.sum(overloads)
overload_probability = overload_count / number_of_simulations

print("\nOriginal simulation")
print("Number of simulations:", number_of_simulations)
print("Server capacity:", capacity)
print("Overload events:", overload_count)
print(f"Estimated overload probability: {overload_probability:.4%}")

# Modification: increase average demand
modified_demand = rng.normal(
    920,
    standard_deviation,
    number_of_simulations
)

modified_probability = np.mean(modified_demand > capacity)

print("\nModified average demand:", 920)
print(f"Modified overload probability: {modified_probability:.4%}")

# Related application: estimate the risk of exceeding a service limit
service_limit = 950
service_risk = np.mean(demand > service_limit)

print("\nRelated application")
print("Service limit:", service_limit)
print(f"Estimated probability of exceeding service limit: {service_risk:.4%}")

# Plot running overload probability
running_probability = np.cumsum(overloads) / np.arange(
    1, number_of_simulations + 1
)

sample_points = np.unique(
    np.logspace(1, np.log10(number_of_simulations), 300).astype(int)
)

plt.plot(sample_points, running_probability[sample_points - 1])
plt.xscale("log")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Server Overload Risk")
plt.grid(True)
plt.show()
