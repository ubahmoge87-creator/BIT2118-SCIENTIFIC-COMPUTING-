
import numpy as np
import timeit

# ============================================================
# TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION
# ============================================================
# Original application: Analyse one million network latency readings.
# Modification: Change the number of readings to 500,000.
# Related application: Analyse sensor response times.
# ============================================================


# ------------------------------------------------------------
# PART 1: ORIGINAL NETWORK-LATENCY EXAMPLE
# ------------------------------------------------------------

# Generate one million simulated latency readings in milliseconds.
# A fixed random seed makes the generated data reproducible.
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)


# Method 1: Use a normal Python loop.
def loop_version():
    squared = []

    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared


# Method 2: Use NumPy vectorization.
def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2


# Measure execution time.
# The loop is run once because it processes one million values.
loop_time = timeit.timeit(loop_version, number=1)

# Run the vectorized version three times and calculate the average.
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Obtain the vectorized results.
result = vectorized_version()

print("PART 1: ORIGINAL NETWORK-LATENCY EXAMPLE")
print("Number of readings:", len(latency_ms))
print("First five squared latency values:", result[:5])
print(f"Python loop time: {loop_time:.4f} seconds")
print(f"Vectorized NumPy time: {vector_time:.4f} seconds")

# Calculate how many times faster vectorization was.
if vector_time > 0:
    print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")


# ------------------------------------------------------------
# PART 2: MODIFICATION OF THE ORIGINAL EXAMPLE
# ------------------------------------------------------------

# Change the number of readings from 1,000,000 to 500,000.
# The readings remain simulated network latency values.
rng_modified = np.random.default_rng(42)
modified_latency_ms = rng_modified.uniform(5, 250, 500_000)


def modified_loop_version():
    squared = []

    for value in modified_latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared


def modified_vectorized_version():
    seconds = modified_latency_ms / 1000.0
    return seconds ** 2


modified_loop_time = timeit.timeit(
    modified_loop_version, number=1
)

modified_vector_time = (
    timeit.timeit(modified_vectorized_version, number=3) / 3
)

modified_result = modified_vectorized_version()

print("\nPART 2: MODIFIED NETWORK-LATENCY EXAMPLE")
print("Number of readings:", len(modified_latency_ms))
print("First five squared latency values:", modified_result[:5])
print(f"Python loop time: {modified_loop_time:.4f} seconds")
print(f"Vectorized NumPy time: {modified_vector_time:.4f} seconds")

if modified_vector_time > 0:
    print(
        "Approximate speed-up:",
        f"{modified_loop_time / modified_vector_time:.1f}x"
    )


# ------------------------------------------------------------
# PART 3: DIFFERENT RELATED APPLICATION
# ------------------------------------------------------------

# Application: Analyse sensor response times.
# Assume a monitoring system records 10,000 sensor responses
# in milliseconds. These readings are simulated.
rng_sensor = np.random.default_rng(7)
sensor_response_ms = rng_sensor.uniform(1, 100, 10_000)

# Convert milliseconds to seconds and square the values.
sensor_response_seconds = sensor_response_ms / 1000.0
squared_sensor_response = sensor_response_seconds ** 2

print("\nPART 3: SENSOR RESPONSE-TIME ANALYSIS")
print("Number of sensor readings:", len(sensor_response_ms))
print(
    "First five squared response times:",
    squared_sensor_response[:5]
)
print(
    "Mean response time:",
    f"{np.mean(sensor_response_ms):.4f} milliseconds"
)
print(
    "Maximum response time:",
    f"{np.max(sensor_response_ms):.4f} milliseconds"
)
