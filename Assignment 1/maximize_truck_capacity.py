import numpy as np
import scipy.optimize as spo
# Problem 1.8

amount_of_truck_a = 0
amount_of_truck_b = 0
amount_of_truck_c = 30

# vector of initial guesses
x0 = [amount_of_truck_a, amount_of_truck_b, amount_of_truck_c]

price_of_truck_a = 10_000
price_of_truck_b = 20_000
price_of_truck_c = 23_000

prices = [price_of_truck_a, price_of_truck_b, price_of_truck_c]

capacity_of_truck_a = 2100
capacity_of_truck_b = 3600
capacity_of_truck_c = 3780

capacities = [capacity_of_truck_a, capacity_of_truck_b, capacity_of_truck_c]

required_drivers_truck_a = 1
required_drivers_truck_b = 2
required_drivers_truck_c = 2

drivers = [required_drivers_truck_a,
           required_drivers_truck_b, required_drivers_truck_c]

maximum_trucks = 30
maximum_drivers = 145
maximum_budget = 600_000


def objective(x: list[float]) -> float:
    """Objective function to minimize

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: total capacity
    """
    return -(x[0]*capacities[0]+x[1]*capacities[1]+x[2]*capacities[2])  # minimum of negative = maximum

def constraint1(x: list[float]) -> float:
    """ineq: maximum amount of trucks

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: number that is >=0 if constraint is obeyed
    """
    return -(x[0]+x[1]+x[2]-maximum_trucks)

def constraint2(x: list[float]) -> float:
    """ineq: maximum amount of drivers
    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: number that is >=0 if constraint is obeyed
    """
    return -(x[0]*drivers[0]+x[1]*drivers[1]+x[2]*drivers[2]-maximum_drivers)

def constraint3(x: list[float]) -> float:
    """ineq: maximum budget

    Args:
        x (list[float]): vector of decision variables

    Returns:
        float: number that is >=0 if constraint is obeyed
    """
    return -(x[0]*prices[0]+x[1]*prices[1]+x[2]*prices[2]-maximum_budget)


def integer_constraint1(x: list[float]) -> float:
    return max([x[0]-int(x[0])])


def integer_constraint2(x: list[float]) -> float:
    return max([x[1]-int(x[1])])


def integer_constraint3(x: list[float]) -> float:
    return max([x[2]-int(x[2])])


bnds = ((0, 30), (0, 30), (0, 30))

# constraints
con1 = {"type": "ineq", "fun": constraint1}
con2 = {"type": "ineq", "fun": constraint2}
con3 = {"type": "ineq", "fun": constraint3}
con4 = {"type": "eq", "fun": integer_constraint1}
con5 = {"type": "eq", "fun": integer_constraint2}
con6 = {"type": "eq", "fun": integer_constraint3}
con7 = {'type':'eq','fun': lambda x : max([x[i]-int(x[i]) for i in range(len(x))])}
cons = [con1, con2, con3]  # list of constraints

# solution
sol = spo.minimize(objective, x0, bounds=bnds, constraints=cons)

print(sol)
print(f'{sol.x[0]+sol.x[1]+sol.x[2] = }')
print(f'{constraint1(sol.x) = }')
print(f'{constraint2(sol.x) = }')
print(f'{constraint3(sol.x) = }')