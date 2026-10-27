
import numpy as np
import matplotlib.pyplot as plt

print("TASK 17: EULER METHOD AND NEWTON'S LAW OF COOLING")

ambient = 25.0
initial_temperature = 90.0
k = 0.12
step = 1.0
end_time = 30.0


def cooling_rate(T):
    return -k * (T - ambient)


# Original example: Euler numerical solution
time = np.arange(0, end_time + step, step)
temperature = np.zeros(len(time))
temperature[0] = initial_temperature

for i in range(1, len(time)):
    temperature[i] = temperature[i-1] + step * cooling_rate(temperature[i-1])

exact = ambient + (initial_temperature - ambient) * np.exp(-k * time)

print("\nOriginal example")
print("Euler temperature at 30 minutes:", temperature[-1])
print("Exact temperature at 30 minutes:", exact[-1])
print("Absolute error:", abs(temperature[-1] - exact[-1]))

# Modification: use a smaller step size
small_step = 0.5
small_time = np.arange(0, end_time + small_step, small_step)
small_temperature = np.zeros(len(small_time))
small_temperature[0] = initial_temperature

for i in range(1, len(small_time)):
    small_temperature[i] = (
        small_temperature[i-1]
        + small_step * cooling_rate(small_temperature[i-1])
    )

print("\nModified step size:", small_step, "minutes")
print("Euler temperature at 30 minutes:", small_temperature[-1])
print("Absolute error:", abs(small_temperature[-1] - exact[-1]))

# Related application: estimate cooling of a hot drink
drink_initial = 80.0
drink_k = 0.08
drink_temperature = np.zeros(len(time))
drink_temperature[0] = drink_initial

for i in range(1, len(time)):
    drink_temperature[i] = drink_temperature[i-1] - step * drink_k * (
        drink_temperature[i-1] - ambient
    )

print("\nHot drink application")
print("Estimated drink temperature after 30 minutes:", drink_temperature[-1])

plt.plot(time, temperature, "o-", label="Euler approximation")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (degrees C)")
plt.title("Newton's Law of Cooling")
plt.legend()
plt.grid(True)
plt.show()
