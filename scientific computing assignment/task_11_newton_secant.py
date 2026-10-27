
import numpy as np
from scipy.optimize import root_scalar

print("TASK 11: NEWTON-RAPHSON AND SECANT METHODS")

cash_flows = np.array([-10000, 3000, 3500, 4000, 2500], dtype=float)


def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))


def derivative(rate):
    return sum(-t * cf / (1 + rate)**(t + 1)
               for t, cf in enumerate(cash_flows) if t > 0)


# Original example: Newton-Raphson
newton = root_scalar(npv, x0=0.10, fprime=derivative, method="newton")
print("\nNewton-Raphson IRR:", newton.root)
print("NPV at Newton root:", npv(newton.root))

# Original example: Secant method
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant")
print("Secant IRR:", secant.root)
print("NPV at secant root:", npv(secant.root))

# Modification: change the final cash flow
modified_flows = cash_flows.copy()
modified_flows[-1] = 3500


def modified_npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(modified_flows))


modified = root_scalar(modified_npv, x0=0.10, x1=0.20, method="secant")
print("\nModified final cash flow:", modified_flows[-1])
print("Modified IRR:", modified.root)
print("Modified NPV:", modified_npv(modified.root))

# Related application: investment evaluation
print("\nInvestment interpretation:")
print("IRR is the discount rate at which the investment NPV is zero.")
print("Compare IRR with the required return before making a decision.")
