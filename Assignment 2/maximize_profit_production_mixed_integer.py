import numpy as np
import scipy.optimize as spo
from scipy.optimize import linprog
from gekko import GEKKO
m = GEKKO(remote = False)
#m.options.Linear = 1 #Tells the solver that the problem in linear

#Problem 1

# variables with bounds

x1 = m.Var(lb=0, ub=None, integer=True)
x2 = m.Var(lb=0, ub=None, integer=True)
x3 = m.Var(lb=0, ub=20, integer=True)

x = [x1,x2,x3]

# inequality constraints

# A[i][j]: i is the index of machine and j is the index of article
A = [[8,2,3],[4,3,0],[2,0,1]] #needed hours per machine per article

milling_machine_time = 200
lathe_time = 100
grinder_time = 50
#maximum available hours per machine
b = [milling_machine_time,lathe_time,grinder_time]

#Maximum available time on each machine
m.Equation(x1*A[0][0]+x2*A[0][1]+x3*A[0][2]<=b[0])
m.Equation(x1*A[1][0]+x2*A[1][1]+x3*A[1][2]<=b[1])
m.Equation(x1*A[2][0]+x2*A[2][1]+x3*A[2][2]<=b[2])

# Objective

c = [200,60,80] #profit per unit
m.Maximize(c[0]*x1+c[1]*x2+c[2]*x3)

#solution
m.options.SOLVER=1
m.solve(disp=True)
print(f'product 1: {x1 = }')
print(f'product 2: {x2 = }')
print(f'product 3: {x3 = }')