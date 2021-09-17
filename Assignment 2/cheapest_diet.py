import numpy as np
import scipy.optimize as spo
from scipy.optimize import linprog
from gekko import GEKKO
m = GEKKO(remote = False)

integer_solutions = False
A = [[1,1,10],[100,10,10],[10,100,10]] #vitamin mg/ration
b = [1,50,10] #minimum daily vitamin
c = [1.0,2.0,0.5] #cost per ration

#decision variables
rations_milk = m.Var(lb=0,ub=None, integer=integer_solutions)
rations_beef = m.Var(lb=0,ub=None, integer=integer_solutions)
rations_egg = m.Var(lb=0,ub=None, integer=integer_solutions)
x = [rations_milk,rations_beef,rations_egg]

#constraints
m.Equation(A[0][0]*x[0]+A[0][1]*x[1]+A[0][2]*x[2] >= 1)
m.Equation(A[1][0]*x[0]+A[1][1]*x[1]+A[1][2]*x[2] >= 50)
m.Equation(A[2][0]*x[0]+A[2][1]*x[1]+A[2][2]*x[2] >= 10)

#objective
m.Minimize(c[0]*x[0]+c[1]*x[1]+c[2]*x[2])

m.options.SOLVER=1
m.solve(disp=True)

print(f'{ x = }')

print(f'{(A[0][0]*x[0][0]+A[0][1]*x[1][0]+A[0][2]*x[2][0]) = }')
print(f'{(A[1][0]*x[0][0]+A[1][1]*x[1][0]+A[1][2]*x[2][0]) = }')
print(f'{A[2][0]*x[0][0]+A[2][1]*x[1][0]+A[2][2]*x[2][0] = }')

