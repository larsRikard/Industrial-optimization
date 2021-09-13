import numpy as np
import scipy.optimize as spo
# problem 1.3


# 1 degree of freedom
# x_length only independant variable
x_lenght = 3
y_height = 10-x_lenght**2

# vector of initial guesses
x0 = [x_lenght, y_height]

def objective(x: list[float]) -> float:
    """Objective function to maximize

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: area
    """
    return -(x[0]*x[1]) #minimizing the negative area is the same as maximizing the positive


def constraint1(x: list[float]) -> float:
    return x[1]+(x[0]**2)-10

# constraints
con1 = {"type": "eq", "fun": constraint1}
cons = [con1]  # list of constraints

# Bound by x axis
bnds = ((None, None), (0, None))

# solution
sol = spo.minimize(objective, x0, bounds=bnds, constraints=cons)

print(sol)
print(f'{sol.x[0]*sol.x[1]*2 = }')

