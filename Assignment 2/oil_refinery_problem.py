import numpy as np
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

B_1 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_2 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_3 = m.Var(lb=0,ub=1, integer=integer_solutions)
B_4 = m.Var(lb=0,ub=1, integer=integer_solutions)

C_1 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_2 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_3 = m.Var(lb=0,ub=1, integer=integer_solutions)
C_4 = m.Var(lb=0,ub=1, integer=integer_solutions)

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
test = []

#Utilization of mix percentage
for i in range(4):
    test.append(m.Equation(const[i]<=const_max[i]))

total_cost = 0
total_sales = 0
for i in range(4):
    total_cost += const[i]*const_cost[i]

for i in range(3):
    total_sales += x[i]*prod_price[i]

profit = total_sales-total_cost
m.Maximize(profit)

m.solve(disp=True)

#Barrels of each product produced
print(f'Amount of each product: { x = }')

#Barrels of each constituent needed
print("total amount of constituents needed:")
print(f'constituent 1: {A_1[0]*x_A[0]+B_1[0]*x_B[0]+C_1[0]*x_C[0]}')
print(f'constituent 2: {A_2[0]*x_A[0]+B_2[0]*x_B[0]+C_2[0]*x_C[0]}')
print(f'constituent 3: {A_3[0]*x_A[0]+B_3[0]*x_B[0]+C_3[0]*x_C[0]}')
print(f'constituent 4: {A_4[0]*x_A[0]+B_4[0]*x_B[0]+C_4[0]*x_C[0]}')

#Optimal blends
print(f'product A mix: c1 = {A_1[0]}, c2 = {A_2[0]}, c3 = {A_3[0]}, c4 = {A_4[0]}')
print(f'product B mix: c1 = {B_1[0]}, c2 = {B_2[0]}, c3 = {B_3[0]}, c4 = {B_4[0]}')
print(f'product C mix: c1 = {C_1[0]}, c2 = {C_2[0]}, c3 = {C_3[0]}, c4 = {C_4[0]}')

#Total profit
print("total profit:")
print(f'{ m.options.OBJFCNVAL = }')
print(f'profit: {profit = }')