import numpy as np
import scipy.optimize as spo
from scipy.optimize import linprog
from gekko import GEKKO
m = GEKKO(remote = False)
#m.options.Linear = 1 #Tells the solver that the problem in linear

#Problem 4

#Farms
farm_A_max_area = 200
farm_B_max_area = 150
farm_C_max_area = 300
area = [200,150,300]

farm_A_max_water = 250
farm_B_max_water = 333
farm_C_max_water = 150
water = [250,333,150]

#Crops
water_per_hectare_1 = 1.6
water_per_hectare_2 = 1.3
water_per_hectare_3 = 1.0
water_per_hectare = [1.6,1.3,1.0]

profit_per_hectare_1 = 800
profit_per_hectare_2 = 600
profit_per_hectare_3 = 100
profit_per_hectare = [800,600,100]

# farm areas with bounds

x1 = m.Var(lb=0, ub=farm_A_max_area, integer=False)
x2 = m.Var(lb=0, ub=farm_B_max_area, integer=False)
x3 = m.Var(lb=0, ub=farm_C_max_area, integer=False)

x = [x1,x2,x3]

# water usage on each farm
""" w1 = m.Var(lb=0, ub=farm_A_max_water, integer=False)
w2 = m.Var(lb=0, ub=farm_B_max_water, integer=False)
w3 = m.Var(lb=0, ub=farm_C_max_water, integer=False)

w = [w1,w2,w3] """

# percentage of each crop type
#Mix percentages (farm A,B,C and crop 1,2,3)
A_1 = m.Var(lb=0,ub=1, integer=False)
A_2 = m.Var(lb=0,ub=1, integer=False)
A_3 = m.Var(lb=0,ub=1, integer=False)

B_1 = m.Var(lb=0,ub=1, integer=False)
B_2 = m.Var(lb=0,ub=1, integer=False)
B_3 = m.Var(lb=0,ub=1, integer=False)

C_1 = m.Var(lb=0,ub=1, integer=False)
C_2 = m.Var(lb=0,ub=1, integer=False)
C_3 = m.Var(lb=0,ub=1, integer=False)

A = [[A_1, B_1, C_1],[A_2,B_2,C_2],[A_3,B_3,C_3]]

# Sum percentage equality constraints
m.Equation(A[0][0]+A[1][0]+A[2][0] == 1)
m.Equation(A[0][1]+A[1][1]+A[2][1] == 1)
m.Equation(A[0][2]+A[1][2]+A[2][2] == 1)


# Same percentage used of each farm
m.Equation(x[0]/area[0] == x[1]/area[1])
m.Equation(x[1]/area[1] == x[2]/area[2])

# water consumption inequality constraint (max water per farm)
# sum(percentage_of_crop_n*needed_water_per_hectar_crop_n)*utilized_area_farm_m


m.Equation((A[0][0]*water_per_hectare[0]+A[1][0]*water_per_hectare[1]+A[2][0]*water_per_hectare[2])*x[0] <= farm_A_max_water)
m.Equation((A[0][1]*water_per_hectare[0]+A[1][1]*water_per_hectare[1]+A[2][1]*water_per_hectare[2])*x[1] <= farm_B_max_water)
m.Equation((A[0][2]*water_per_hectare[0]+A[1][2]*water_per_hectare[1]+A[2][2]*water_per_hectare[2])*x[2] <= farm_C_max_water)

""" m.Equation((A_1*water_per_hectare_1+A_2*water_per_hectare_2+A_3*water_per_hectare_3)*x1 <= farm_A_max_water)
m.Equation((B_1*water_per_hectare_1+B_2*water_per_hectare_2+B_3*water_per_hectare_3)*x2 <= farm_B_max_water)
m.Equation((C_1*water_per_hectare_1+C_2*water_per_hectare_2+C_3*water_per_hectare_3)*x3 <= farm_C_max_water) """


# Objective

profit = 0

for i in range(3):
    for j in range(3):
        profit += x[i]*A[i][j]*profit_per_hectare[i]

m.Maximize(profit)

#solution
m.options.SOLVER=1
m.solve(disp=True)

#Utilized percentage of farms:
print(f'Utilization of farm 1: {x[0][0]/area[0]}')
print(f'Utilization of farm 2: {x[1][0]/area[1]}')
print(f'Utilization of farm 3: {x[2][0]/area[2]}')

#Crop percentage on each farm:
print(f'Crop split of farm 1. Crop 1: {A[0][0][0]}, crop 2: {A[1][0][0]}, crop 3: {A[2][0][0]}')
print(f'Crop split of farm 2. Crop 1: {A[0][1][0]}, crop 2: {A[1][1][0]}, crop 3: {A[2][1][0]}')
print(f'Crop split of farm 3. Crop 1: {A[0][2][0]}, crop 2: {A[1][2][0]}, crop 3: {A[2][2][0]}')

#Water utilization
print(f'Water usage farm 1: {(A[0][0][0]*water_per_hectare[0]+A[1][0][0]*water_per_hectare[1]+A[2][0][0]*water_per_hectare[2])*x[0][0]} <= {farm_A_max_water}')
print(f'Water usage farm 2: {(A[0][1][0]*water_per_hectare[0]+A[1][1][0]*water_per_hectare[1]+A[2][1][0]*water_per_hectare[2])*x[1][0]} <= {farm_B_max_water}')
print(f'Water usage farm 3: {(A[0][2][0]*water_per_hectare[0]+A[1][2][0]*water_per_hectare[1]+A[2][2][0]*water_per_hectare[2])*x[2][0]} <= {farm_C_max_water}')

profit_maxed = 0
for i in range(3):
    for j in range(3):
        profit_maxed += x[i][0]*A[i][j][0]*profit_per_hectare[i]

print(f'{profit_maxed = }')