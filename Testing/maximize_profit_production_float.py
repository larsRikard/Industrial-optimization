import numpy as np
import scipy.optimize as spo
from scipy.optimize import linprog

#Problem 1

# Objective

c = [-200,-60,-80] #profit per unit

# inequality constraints

# A[i][j]: i is the index of machine and j is the index of article
A = [[8,2,3],[4,3,0],[2,0,1]] #needed hours per machine per article

milling_machine_time = 200
lathe_time = 100
grinder_time = 50
#maximum available hours per machine
b = [milling_machine_time,lathe_time,grinder_time]

# equality constraints

# no equality constraints

#bounds
x0_bounds = (0, None) #no negatives
x1_bounds = (0, None)
x2_bounds = (0, 20) #maximum sales potential for product 3
bnds = [x0_bounds,x1_bounds,x2_bounds]


#solution

res = linprog(c, A_ub=A, b_ub=b, bounds=bnds, method="revised simplex")

print(res)