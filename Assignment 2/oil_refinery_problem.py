import numpy as np
import scipy.optimize as spo
from scipy.optimize import linprog
from gekko import GEKKO
m = GEKKO(remote = False)

integer_solutions = False

const_max = [3000,2000,4000,1000]
const_cost = [3.0,6.0,4.0,5.0]

prod_price = [5.50,4.50,3.50]

#Mix percentages
A_1 = m.Var(lb=0,ub=1, integer=integer_solutions)
A_2 = m.Var(lb=0,ub=1, integer=integer_solutions)
A_3 = m.Var(lb=0,ub=1, integer=integer_solutions)
A_4 = m.Var(lb=0,ub=1, integer=integer_solutions)

C_1 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_2 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_3 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_4 = m.Var(lb=0,ub=1, integer=integer_solutions)

B_1 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_2 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_3 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_4 = m.Var(lb=0,ub=1, integer=integer_solutions)

A = [[A_1, B_1, C_1],[A_2,B_2,C_2],[A_3,B_3,C_3],[A_4,B_4,C_4]]

#Amount of each product
x_A = m.Var(lb=0,ub=None)
x_B = m.Var(lb=0,ub=None)
x_C = m.Var(lb=0,ub=None)

x = [x_A,x_B,x_C]

#Sum percentage equality constraints
m.Equation(A_1+A_2+A_3+A_4 == 1)
m.Equation(B_1+B_2+B_3+B_4 == 1)
m.Equation(C_1+C_2+C_3+C_4 == 1)

#Min/Max mix inequality constraints 
m.Equation(A_1 <= 0.3)
m.Equation(A_2 >= 0.4)
m.Equation(A_3 <= 0.5)

m.Equation(B_1 <= 0.5)
m.Equation(B_2 >= 0.1)

m.Equation(C_1 <= 0.7)

#Amount of constituents needed
const_1 = A_1*x_A+B_1*x_B+C_1*x_C
const_2 = A_2*x_A+B_2*x_B+C_2*x_C
const_3 = A_3*x_A+B_3*x_B+C_3*x_C
const_4 = A_4*x_A+B_4*x_B+C_4*x_C

const = [const_1, const_2, const_3, const_4]

#Utilization of mix percentage
for i in range(4):
    m.Equation(const[i]<=const_max[i])

total_cost = 0
total_sales = 0
for i in range(4):
    total_cost += const[i]*const_cost[i]

for i in range(3):
    total_sales += x[i]*prod_price[i]

m.Maximize(total_sales-total_cost)

m.solve(disp=True)

print(f'{ x = }')
print(f'{ const[0] = }')
print(f'{ const[1] = }')
print(f'{ const[2] = }')
print(f'{ const[3] = }')
print(f'{ m.sol = }')


""" print(m.path)

import json
with open(m.path+'//results.json') as f:
    results = json.load(f) """






