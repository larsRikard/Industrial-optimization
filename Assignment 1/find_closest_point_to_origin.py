from math import sqrt
import numpy as np
import scipy.optimize as spo
# problem 1.5

x_value = 2

# vector of initial guesses
x0 = [x_value]

def objective(x: list[float]) -> float:
    """Objective function to maximize

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: area
    """
    y = (2*x[0]**2)+3*x+1
    # pythagoras
    distance_from_origin = (x[0]**2)+(y**2)
    return distance_from_origin

# solution
sol = spo.minimize(objective, x0, bounds=None, constraints=None)

print(sol)

print(f'The closes point to origin is at x = {sol.x[0]}, y = {sol.fun}')

