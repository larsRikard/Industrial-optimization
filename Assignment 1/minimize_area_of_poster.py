import numpy as np
import scipy.optimize as spo
# problem 1.1

def objective(x: list[float]) -> float:
    """function to minimize

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: result of the function, minimize this value
    """
    return (x[0]+8)*(x[1]+12)


def constraint1(x: list[float]) -> float:
    """equality constraint: area should equal 300

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: value that should be zero or very very close
    """
    return x[0]*x[1]-300


# initial guess
x0 = [6, 6]

# constraints
con1 = {"type": "eq", "fun": constraint1}
cons = [con1]  # list of constraints

# solution
sol = spo.minimize(objective, x0, constraints=cons)

# print of the solution
print(sol)

# checking if the solution obeys the constraints
print(f'{sol.x[0]*sol.x[1] = }')
