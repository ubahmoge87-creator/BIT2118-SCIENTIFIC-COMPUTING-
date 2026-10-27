
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

print("TASK 14: CURVE FITTING")

# Original example: response time versus user load
users = np.array([10, 20, 30, 40, 50, 60], dtype=float)
response_ms = np.array([105, 120, 142, 170, 205, 245], dtype=float)


def model(x, a, b):
    return a * np.exp(b * x)


parameters, _ = curve_fit(model, users, response_ms, p0=[90, 0.015])
a, b = parameters

print("\nOriginal fitted parameters:", parameters)
print("Predicted response at 45 users:", float(model(45, a, b)))

# Modification: fit using a changed observation
modified_response = response_ms.copy()
modified_response[-1] = 260
modified_parameters, _ = curve_fit(
    model, users, modified_response, p0=[90, 0.015]
)
print("\nModified final observation:", modified_response[-1])
print("Modified fitted parameters:", modified_parameters)

# Related application: estimate response time for a new load
future_users = 70
predicted = model(future_users, *parameters)
print("\nEstimated response time at", future_users,
      "users:", round(float(predicted), 2), "ms")

x_plot = np.linspace(users.min(), 75, 200)
plt.scatter(users, response_ms, label="Observed data")
plt.plot(x_plot, model(x_plot, *parameters), label="Fitted curve")
plt.xlabel("Number of users")
plt.ylabel("Response time (ms)")
plt.title("Server Response-Time Curve Fitting")
plt.legend()
plt.grid(True)
plt.show()
