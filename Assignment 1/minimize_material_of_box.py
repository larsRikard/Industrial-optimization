import numpy as np
import scipy.optimize as spo
# problem 1.2

# 1 degree of freedom, because changing one variable all others have to obey the constraints
# Width/length independant variables but they are the same variable in this case
box_width = 22
box_length = box_width
box_height = 3

# vector of initial guesses
x0 = [box_width, box_length, box_height]


def objective(x: list[float]) -> float:
    """Objective function to minimize

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: sum of area
    """
    base_area = x[0]*x[1]
    side_area_1 = x[0]*x[2]
    side_area_2 = x[1]*x[2]
    return base_area+side_area_1*2+side_area_2*2


def constraint1(x: list[float]) -> float:
    return x[0]*x[1]*x[2]-1000


# constraints
con1 = {"type": "eq", "fun": constraint1}
cons = [con1]  # list of constraints

# solution
sol = spo.minimize(objective, x0, constraints=cons)

print(sol)
print(f'{sol.x[0]*sol.x[1]*sol.x[2] = }')

