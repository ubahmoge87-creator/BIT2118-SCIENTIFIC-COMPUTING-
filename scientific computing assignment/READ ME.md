# Scientific Computing Assignment

## Task 2: NumPy Arrays and Numerical Computation

### Objective

To use NumPy arrays to store temperature readings, calculate basic statistics, and convert temperatures from Celsius to Fahrenheit.

### Input Data

The program uses 24 hourly temperature readings measured in degrees Celsius.

### Original Example

The original program calculates the daily mean, minimum and maximum temperatures and converts the readings to Fahrenheit.

### Modification Made

The fourth temperature reading was changed from 17.5°C to 10.0°C. This modification was made to investigate how a lower temperature reading affects the statistical results.

### Results and Interpretation

- The daily mean temperature decreased.
- The minimum temperature changed from 17.5°C to 10.0°C.
- The maximum temperature remained at 29.4°C because the highest reading was not changed.
- The Fahrenheit conversion was performed using the formula F = 1.8C + 32.

### Conclusion

NumPy makes it possible to perform calculations on an array of numerical values efficiently. Changing an input value affects the calculated results, demonstrating the importance of input data in numerical computation.

### Library Used

NumPy

## Task 3: Mathematical Functions and Vectorization

### Objective

To understand vectorization and compare the execution time of a normal Python loop with NumPy vectorized operations.

### Input Data

The program generates 1,000,000 simulated network latency readings between 5 and 250 milliseconds using NumPy.

### Mathematical Operation

Each latency reading is converted from milliseconds to seconds by dividing by 1,000. The resulting value is squared.

\[
\text{Squared latency}=\left(\frac{\text{Latency in milliseconds}}{1000}\right)^2
\]

### Modification Made

I modified the original example by testing NumPy vectorization with a smaller dataset of 100,000 readings selected from the original one million readings.

### Results

- Python loop execution time: 0.5158 seconds.
- NumPy vectorized execution time for 1,000,000 readings: 0.0109 seconds.
- Approximate speed-up: 47.4 times.
- NumPy vectorized execution time for 100,000 readings: 0.0024 seconds.

### Interpretation

The Python loop processes each reading individually, whereas NumPy vectorization performs the calculation on an entire array without an explicit Python loop. In my test, the vectorized version processed one million readings approximately 47.4 times faster than the loop version. Processing 100,000 readings also took less time than processing one million readings.

### Conclusion

NumPy vectorization is useful for numerical computing because it can process large datasets efficiently. The measured execution times may vary depending on the computer and its workload.

# Task 4: Floating-Point Errors and Numerical Stability

## 1. Objective

The objective of this task is to understand floating-point errors, calculate absolute and relative errors, compare numerical formulas, and apply numerical accuracy checks to a real-world temperature sensor.

## 2. Original Problem

The original program demonstrates three concepts:

1. Floating-point comparison using 0.1 + 0.2 and 0.3.
2. Absolute and relative error using the square root of 2.
3. Numerical stability by comparing two mathematically equivalent formulas.

## 3. Input Values

### Floating-point comparison

- First number: 0.1
- Second number: 0.2
- Expected result: 0.3

### Error calculation

- True value: square root of 2
- Original approximate value: 1.414
- Modified approximate value: 1.4142

### Numerical stability

The values of x are 0.0001, 0.00000001, and 0.000000000001.

### Temperature sensor application

- Reference temperature: 25.0 degrees Celsius
- Measured temperature: 24.98 degrees Celsius
- Allowed error: 0.05 degrees Celsius

## 4. Mathematical Operations

### Floating-point comparison

The program calculates:

0.1 + 0.2

Computers store many decimal numbers as binary floating-point approximations. Therefore, the calculated result may not be exactly equal to 0.3.

The function np.isclose() checks whether two values are sufficiently close.

### Absolute error

Absolute error is calculated using:

Absolute error = |True value - Approximate value|

### Relative error

Relative error is calculated using:

Relative error = Absolute error / |True value|

Relative error expresses the size of the error compared with the true value.

### Numerical stability

The program compares:

Direct formula:
(sqrt(1 + x) - 1) / x

Stable formula:
1 / (sqrt(1 + x) + 1)

These formulas are mathematically equivalent when x is nonzero and the expressions are defined.

The direct formula may lose precision when x is extremely small because it subtracts two numbers that are very close together. This is called cancellation error.

## 5. Python Libraries and Functions

- NumPy: Performs numerical calculations.
- np.sqrt(): Calculates a square root.
- np.isclose(): Compares floating-point values within a tolerance.
- abs(): Calculates absolute error.
- A for loop: Tests multiple values of x.

## 6. Modification Made

The original approximation of the square root of 2 is 1.414.

The modified approximation is 1.4142.

The program calculates the absolute and relative errors for both approximations.

The improved approximation should produce a smaller error because it is closer to the true value.

## 7. Related Real-World Application

The modified application checks the accuracy of a temperature sensor.

The reference temperature is 25.0 degrees Celsius, while the sensor measures 24.98 degrees Celsius.

The allowed difference is 0.05 degrees Celsius.

The program calculates the absolute and relative errors and checks whether the measured temperature is within the allowed tolerance.

This example assumes that the reference temperature is accurate and that the specified tolerance is appropriate for the application.

## 8. Expected Results and Interpretation

- The exact comparison between 0.1 + 0.2 and 0.3 is normally False.
- The tolerance-based comparison is True.
- The improved approximation of the square root of 2 has a smaller error.
- The direct numerical formula may become less accurate for very small values of x.
- The temperature sensor has an absolute error of 0.02 degrees Celsius.
- Since 0.02 is less than the allowed error of 0.05 degrees Celsius, the sensor reading is acceptable.

The exact numerical results can vary slightly depending on floating-point calculations and the computer environment.

## 9. Conclusion

This task demonstrates why floating-point numbers should not always be compared using exact equality. It also shows how absolute error, relative error, and tolerance checks help assess numerical accuracy.

The comparison of equivalent formulas demonstrates the importance of choosing numerically stable methods. The temperature sensor example applies these concepts to a practical measurement problem.

## 10. How to Run the Program

1. Save the Python program as Task_04_floating_point_errors.py.
2. Ensure Python and NumPy are installed.
3. Open the terminal in the folder containing the program.
4. Run:

python Task_04_floating_point_errors.py

# Task 5: Matrix Algebra and Geometric Transformations

## 1. Objective

The objective of this task is to understand how matrices represent geometric transformations, including rotation and scaling, and how matrix multiplication combines these transformations.

## 2. Original Problem

The original program represents the four corners of a square using a NumPy array.

The square is rotated by 45 degrees and scaled by different amounts along the x-axis and y-axis.

The program calculates the transformed coordinates and the determinant of the combined transformation matrix.

## 3. Input Values

The original square has four points:

- (0, 0)
- (1, 0)
- (1, 1)
- (0, 1)

The rotation angle is 45 degrees.

The scale factors are:

- x-axis: 2
- y-axis: 1.5

## 4. Mathematical Operations

### Rotation matrix

For an angle θ, the rotation matrix is:

R = [[cos θ, -sin θ], [sin θ, cos θ]]

The angle is converted from degrees to radians before calculating sine and cosine.

### Scaling matrix

The original scaling matrix is:

S = [[2, 0], [0, 1.5]]

This doubles the x-coordinate and multiplies the y-coordinate by 1.5.

### Combined transformation

The program combines the matrices using:

T = R × S

The transformed coordinates are calculated using:

Transformed points = Original points × T transpose

The transpose is used because each point is stored as a row in the NumPy array.

### Determinant

The determinant indicates whether the transformation preserves area, changes area, or collapses the shape.

For the original transformation, the determinant is:

det(T) = 2 × 1.5 = 3

Rotation does not change area, while scaling multiplies the area by the product of the scale factors.

## 5. Python Libraries and Functions

- NumPy: Stores coordinates and performs matrix calculations.
- np.array(): Creates arrays and matrices.
- np.radians(): Converts degrees to radians.
- np.cos() and np.sin(): Calculate trigonometric values.
- The @ operator: Performs matrix multiplication.
- np.linalg.det(): Calculates a matrix determinant.
- np.round(): Rounds displayed coordinates.

## 6. Modification Made

The original rotation angle of 45 degrees is changed to 30 degrees.

The original scale factors of 2 and 1.5 are changed to 1.5 and 0.75.

The program calculates the new transformation matrix and transformed coordinates.

These changes produce a different orientation and size for the transformed square.

## 7. Related Real-World Application

The related application demonstrates the rotation of a rectangular robot boundary.

The rectangle has four boundary coordinates:

- (2, 1)
- (4, 1)
- (4, 3)
- (2, 3)

The program rotates the rectangle by 90 degrees around the origin.

The scaling matrix uses scale factors of 1 on both axes, so the robot boundary retains its size.

This example assumes the robot's boundary is represented by a two-dimensional coordinate system and the rotation occurs around the origin.

## 8. Expected Results and Interpretation

The original transformation determinant is approximately 3.

This means the original square's area is multiplied by a factor of 3.

The modified transformation determinant is approximately 1.125 because:

1.5 × 0.75 = 1.125

The modified square therefore has a smaller area than the original transformed square.

In the robot example, the coordinates change because of the 90-degree rotation, but the rectangle's size remains unchanged.

Small numerical differences may appear because of floating-point calculations.

## 9. Conclusion

This task demonstrates how matrix multiplication can combine rotation and scaling into a single transformation.

The determinant helps explain how a transformation affects area. The robot example shows how the same mathematical principles can be applied to objects represented in a two-dimensional coordinate system.

## 10. How to Run the Program

1. Save the Python code as Task_05_matrix_algebra.py.
2. Ensure Python and NumPy are installed.
3. Open the terminal in the folder containing the program.
4. Run:

python Task_05_matrix_algebra.py

# Task 6: Solving Linear Systems Using NumPy

## 1. Objective

The objective is to solve simultaneous linear equations using NumPy and apply the solution to resource allocation problems.

## 2. Original Problem

The original example determines the number of two types of servers that use available CPU and memory resources.

Let:

- x = number of Type A servers
- y = number of Type B servers

Each Type A server uses 4 CPU units and 8 GB of memory.

Each Type B server uses 2 CPU units and 12 GB of memory.

The available resources are 20 CPU units and 72 GB of memory.

The equations are:

4x + 2y = 20

8x + 12y = 72

## 3. Input Values

The coefficient matrix is:

A = [[4, 2], [8, 12]]

The resource vector is:

b = [20, 72]

The program uses these values to solve for x and y.

## 4. Mathematical Operation

The simultaneous equations are written in matrix form:

Ax = b

The solution is calculated using:

np.linalg.solve(A, b)

This function solves the system of linear equations without explicitly calculating the inverse of the matrix.

The residual is calculated using:

Residual = A × solution - b

A residual close to zero indicates that the calculated solution satisfies the equations, allowing for small floating-point errors.

## 5. Python Libraries and Functions

- NumPy: Performs numerical calculations.
- np.array(): Creates the coefficient matrix and resource vector.
- np.linalg.solve(): Solves the simultaneous equations.
- The @ operator: Performs matrix multiplication.

## 6. Modification Made

The available CPU resources are changed from 20 to 28 units.

The available memory is changed from 72 GB to 96 GB.

The program solves the equations again using the modified resource vector.

This demonstrates how changing the available resources affects the number of servers in the mathematical model.

## 7. Related Real-World Application

The related application calculates production quantities for two products in a factory.

Let:

- x = quantity of Product A
- y = quantity of Product B

Product A requires 2 machine-hours and 1 labour-hour.

Product B requires 1 machine-hour and 3 labour-hours.

The factory has 11 machine-hours and 13 labour-hours available.

The equations are:

2x + y = 11

x + 3y = 13

The program solves these equations and checks the resources used.

The model assumes the resource requirements per product are fixed and that the available machine and labour hours are fully used.

## 8. Expected Results and Interpretation

For the original server problem:

- Type A servers = 1.5
- Type B servers = 7

For the modified server problem:

- Type A servers = 3
- Type B servers = 8

For the factory application:

- Product A = 4
- Product B = 3

The mathematical solutions satisfy their respective equations.

Fractional server quantities are useful for mathematical analysis but cannot represent actual whole servers. In real deployment, server counts would need to be integers, and additional resource constraints might be necessary.

## 9. Conclusion

This task demonstrates how NumPy solves simultaneous linear equations. The server example shows how linear algebra can model computing resource allocation, while the factory example applies the same method to production planning.

## 10. How to Run the Program

1. Save the Python program as Task_06_linear_systems.py.
2. Ensure Python and NumPy are installed.
3. Open the terminal in the folder containing the program.
4. Run:

python Task_06_linear_systems.py

# Task 7: Gaussian Elimination and LU Decomposition

## Objective

Solve systems of linear equations and compare solutions using NumPy and SciPy.

## Original Problem

The coefficient matrix is:
A = [[4, -1, 0], [-1, 4, -1], [0, -1, 3]]

The original measurement vector is [15, 10, 10].

The system is written as Ax = b.

## Mathematical Operations

`np.linalg.solve()` solves the original system.
`lu_factor()` decomposes the matrix into LU factors.
`lu_solve()` uses the factorization to solve a system.
The residual `A @ solution - b` checks solution accuracy.

## Modification

The measurement vector changes to [16, 11, 9]. The program solves the modified system using the same LU factorization.

## Related Application

The same matrix is used to estimate values for three connected zones from readings [14, 12, 11]. This is an illustrative linear model, not a calibrated physical model.

## Interpretation

Residuals close to zero indicate that the calculated solution satisfies the equations. LU factorization is useful when solving multiple systems with the same coefficient matrix.

## How to Run

Install NumPy and SciPy, then run:
`python Task_07_lu_decomposition.py`

# Task 8: Jacobi and Gauss-Seidel Iterative Methods

## Objective

Approximate the solution of a linear system using two iterative numerical methods.

## Original Problem

A five-variable system represents a simplified grid-temperature model. The matrix is tridiagonal, and the original vector is [100, 0, 0, 0, 20].

## Mathematical Operations

The Jacobi method calculates each new value using values from the previous iteration.
The Gauss-Seidel method uses newly calculated values immediately.
The direct solution from `np.linalg.solve()` provides a comparison.

## Modification

The boundary vector changes to [80, 0, 0, 0, 30], and both iterative methods calculate a new solution.

## Related Application

A second boundary vector [60, 0, 0, 0, 10] illustrates temperature values along a simplified rod. The model assumes the matrix correctly represents the relationships between points.

## Interpretation

The iterative answers should be close to the direct solution for the original system. Small residuals indicate that the equations are approximately satisfied.

## How to Run

Install NumPy and run:
`python Task_08_iterative_methods.py`

# Task 9: Eigenvalues and Eigenvectors

## Objective

Use eigenvalues and eigenvectors to analyse a network represented by an adjacency matrix.

## Original Problem

The matrix represents connections between four nodes, A, B, C, and D. A value of 1 indicates a connection; 0 indicates no connection.

## Mathematical Operations

`np.linalg.eig()` calculates eigenvalues and eigenvectors.
The eigenvector associated with the largest eigenvalue is used to calculate a simple centrality score. Absolute values are normalized so the scores sum to 1.

## Modification

A connection between nodes A and D is added. The program recalculates the largest eigenvalue and centrality scores.

## Related Application

The scores are used to rank four connected service stations in an illustrative network. Higher scores indicate greater importance according to this network model.

## Interpretation

Adding a connection can change the network's eigenvalues and the relative centrality of its nodes. The scores depend on the chosen network representation.

## How to Run

Install NumPy and run:
`python Task_09_eigenvalues.py`

# Task 10: Root Finding

## Objective

Find a value where a nonlinear function equals zero using numerical methods.

## Original Problem

The heat-balance function is `T - 25 - 10 * exp(-T/20)`. The program finds its root within the interval [20, 40].

## Mathematical Operations

SciPy's `root_scalar()` uses bisection to find a root.
Fixed-point iteration repeatedly calculates `T = 25 + 10 * exp(-T/20)` until successive values differ by less than the tolerance.
Matplotlib plots the function and its root.

## Modification

The heat-input coefficient changes from 10 to 15, and the root is recalculated.

## Related Application

The root represents an equilibrium temperature in a simplified heat-balance model. This is an illustrative model; real systems require validated physical parameters.

## Interpretation

At the root, the heat-balance function is approximately zero. The plotted intersection with the horizontal axis shows the root visually.

## How to Run

Install NumPy, SciPy, and Matplotlib, then run:
`python Task_10_root_finding.py`

# Task 11: Newton-Raphson and Secant Methods

## Objective

Find the internal rate of return (IRR) by solving for the discount rate at which net present value (NPV) equals zero.

## Original Problem

Cash flows are [-10000, 3000, 3500, 4000, 2500]. The first value represents the initial investment; subsequent values represent future cash flows.

## Mathematical Operations

NPV is calculated by discounting each cash flow by `(1 + rate)**t`.
Newton-Raphson uses the derivative of NPV. The secant method estimates the derivative using two starting values.

## Modification

The final cash flow changes from 2500 to 3500, and the IRR is recalculated.

## Related Application

The calculation illustrates how investors can evaluate a proposed investment. Actual decisions should also consider risk, timing, and other financial factors.

## Interpretation

The IRR is the rate at which NPV is approximately zero. The two methods should normally produce similar roots when they converge to the same solution.

## How to Run

Install NumPy and SciPy, then run:
`python Task_11_newton_secant.py`

# Task 12: Solving Nonlinear Equations

## Objective

Find simultaneous solutions to a system of nonlinear equations.

## Original Problem

The equations describe intersections between a circle, `x² + y² = 4`, and a parabola, `y = x² - 1`.

## Mathematical Operations

The equations are rewritten so each expression equals zero. SciPy's `root()` function estimates values of x and y that satisfy both equations.

## Modification

Different initial guesses are used to test whether the solver converges to a solution.

## Related Application

The same mathematical method can help find intersections between two design constraints. The equations here are illustrative and do not represent a specific engineered device.

## Interpretation

A successful result with residuals close to zero indicates that both equations are satisfied approximately. Different starting guesses may converge to different intersections.

## How to Run

Install NumPy and SciPy, then run:
`python Task_12_nonlinear_equations.py`

# Task 13: Interpolation

## Objective

Estimate values between known data points using linear interpolation and cubic splines.

## Original Problem

Hourly temperatures are provided from 08:00 to 14:00. The program estimates the temperature at 10:30.

## Mathematical Operations

`interp1d()` performs linear interpolation.
`CubicSpline()` creates a smooth piecewise cubic curve through the observed points.

## Modification

The estimated time changes from 10:30 to 11:30.

## Related Application

The program estimates a missing temperature-sensor reading at 12:30. This assumes the temperature changes smoothly between observations.

## Interpretation

The two methods can return slightly different estimates because they use different interpolation approaches. Estimates between measured points are not additional observations.

## How to Run

Install NumPy, SciPy, and Matplotlib, then run:
`python Task_13_interpolation.py`

# Task 14: Curve Fitting

## Objective

Fit a mathematical curve to observed data and use it to estimate values.

## Original Problem

The example models server response time against the number of users. The data contains six user-load and response-time observations.

## Mathematical Operations

`curve_fit()` estimates the parameters of an exponential model, `a * exp(b*x)`, that best fits the observations in a least-squares sense.

## Modification

The last response-time observation changes from 245 ms to 260 ms, and the curve is fitted again.

## Related Application

The fitted curve estimates response time at 70 users. This is an illustrative prediction and should not be treated as a reliable capacity forecast without more data.

## Interpretation

Changing an observation can change the fitted parameters. Predictions outside the observed range are extrapolations and may be less reliable.

## How to Run

Install NumPy, SciPy, and Matplotlib, then run:
`python Task_14_curve_fitting.py`

# Task 15: Numerical Differentiation

## Objective

Estimate derivatives numerically to determine velocity and acceleration from position data.

## Original Problem

The position function is `3*t² + 2*t`. The program estimates velocity and acceleration over a time interval.

## Mathematical Operations

Velocity is the derivative of position with respect to time. Acceleration is the derivative of velocity. NumPy's `gradient()` estimates derivatives from sampled data.

## Modification

The position function changes to `2*t² + 4*t`, and the derivatives are recalculated.

## Related Application

The program estimates vehicle speed from a position function. In real applications, measured positions may contain noise.

## Interpretation

The numerical estimates approximate the derivatives. Results near the endpoints can be less accurate because fewer neighbouring points are available.

## How to Run

Install NumPy and Matplotlib, then run:
`python Task_15_numerical_differentiation.py`

# Task 16: Numerical Integration

## Objective

Estimate the area under a sampled curve using numerical integration.

## Original Problem

Power readings in kilowatts are recorded every two hours over a 12-hour period. Integrating power over time estimates energy in kilowatt-hours.

## Mathematical Operations

`np.trapezoid()` uses the trapezoidal rule.
`scipy.integrate.simpson()` uses Simpson's rule to estimate the integral.

## Modification

All original power readings are increased by 20%, and the energy is recalculated.

## Related Application

The program estimates energy generated by a solar system using a set of power readings over 12 hours.

## Interpretation

The methods may produce slightly different estimates because they approximate the area differently. Energy estimates depend on the accuracy and frequency of the input measurements.

## How to Run

Install NumPy and SciPy, then run:
`python Task_16_numerical_integration.py`

If your NumPy version does not support `np.trapezoid()`, upgrade NumPy or replace it with `np.trapz()`.

# Task 17: Euler Method and Newton's Law of Cooling

## Objective

Approximate the solution of a differential equation using Euler's method.

## Original Problem

An object starts at 90°C in an environment at 25°C. The cooling coefficient is 0.12 per minute, and the time step is one minute.

## Mathematical Operations

Newton's law of cooling is represented by `dT/dt = -k(T - ambient)`.
Euler's method estimates the next temperature using the current temperature and cooling rate.
The exact solution is used to measure numerical error.

## Modification

The time step is reduced from one minute to half a minute.

## Related Application

The same method estimates the cooling of a hot drink initially at 80°C, using a cooling coefficient of 0.08 per minute.

## Interpretation

A smaller time step generally improves Euler's approximation for this problem. The cooling coefficients are illustrative assumptions, not measured values.

## How to Run

Install NumPy and Matplotlib, then run:
`python Task_17_euler_cooling.py`

# Task 18: Solving an ODE with SciPy

## Objective

Solve an ordinary differential equation using SciPy's numerical integration solver.

## Original Problem

The example models a capacitor charging from a 5 V supply through a 1000-ohm resistor with a capacitance of 0.001 farads.

## Mathematical Operations

The differential equation is `dV/dt = (Vs - V)/(R*C)`.
`solve_ivp()` calculates the voltage over time.
The analytical solution is used to check numerical accuracy.

## Modification

The capacitance is changed from 0.001 F to 0.002 F.

## Related Application

The simulation illustrates capacitor charging in an RC electronic circuit.

## Interpretation

A larger capacitance increases the time constant `R*C`, so the capacitor generally charges more slowly. The plotted curves show this difference.

## How to Run

Install NumPy, SciPy, and Matplotlib, then run:
`python Task_18_solve_ivp.py`

# Task 19: Numerical Optimization

## Objective

Minimize operating cost while meeting a required capacity.

## Original Problem

Type A servers cost 12 units and provide 100 capacity units. Type B servers cost 18 units and provide 170 capacity units. The required capacity is 1000 units.

## Mathematical Operations

The objective function is `12*x + 18*y`.
The constraint is `100*x + 170*y >= 1000`.
SciPy's `minimize()` with SLSQP finds a numerical solution subject to non-negative bounds.

## Modification

The required capacity increases from 1000 to 1500 units.

## Related Application

The program also searches whole-number combinations of servers and selects the lowest-cost combination meeting the original capacity requirement.

## Interpretation

The optimization result estimates the least-cost solution for the mathematical model. Actual servers must be whole units, so the integer search is more realistic for deployment than a continuous solution. Costs and capacities are illustrative.

## How to Run

Install NumPy and SciPy, then run:
`python Task_19_optimization.py`

# Task 20: Monte Carlo Simulation

## Objective

Estimate the probability of server overload using repeated random simulations.

## Original Problem

Server demand is modelled using a normal distribution with mean 850 and standard deviation 120. Server capacity is 1000 units. The program performs 100,000 simulations.

## Mathematical Operations

NumPy generates random demand values.
An overload occurs when demand exceeds capacity.
The estimated probability is the number of overload events divided by the total number of simulations.

## Modification

The average demand increases from 850 to 920 units while capacity and standard deviation remain unchanged.

## Related Application

The program estimates the probability that demand exceeds a service limit of 950 units. This can illustrate how a service operator might assess capacity risk.

## Interpretation

Increasing average demand generally increases overload risk. The running-probability plot shows how the estimate changes as more simulations are included. The result is an estimate, not an exact probability.

## Assumptions

Demand is assumed to follow a normal distribution with the specified mean and standard deviation. Real server demand may follow a different distribution and should be modelled using suitable historical data.

## How to Run

Install NumPy and Matplotlib, then run:
`python Task_20_monte_carlo.py`
