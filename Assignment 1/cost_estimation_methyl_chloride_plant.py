import numpy as np
import numpy_financial as npf
import scipy.optimize as spo

#Comparison of chlorinators

#interest rates
interest_rates = [0.1,0.2]

#period in years: year zero to year 10
period = 11

#Glass-linted chlorinator:
gl_installed_cost = 24_000
gl_life_estimate = 10
gl_salvage_value = 4000
gl_annual_cost = gl_installed_cost*0.1
gl_yearly_premium = 1700

gl_maintenance_cost = np.zeros(period)
gl_maintenance_cost[2] = 230 #maintenance cost at end of 2nd year
gl_maintenance_cost[5] = 560 #maintenance cost at end of 5th year

for i in range(6,len(gl_maintenance_cost)):
    gl_maintenance_cost[i] = 900 #maintenece cost at the end of the rest of the years

gl_money_flow = np.zeros(period)
gl_money_flow[0] -= gl_installed_cost #initial cost

for i in range(1, len(gl_money_flow)):
    gl_money_flow[i] -= gl_annual_cost
    gl_money_flow[i] -= gl_maintenance_cost[i]
    gl_money_flow[i] += gl_yearly_premium
    if(i%10 == 0):
        gl_money_flow[i] += gl_salvage_value

gl_npv_10_percent = npf.npv(interest_rates[0], gl_money_flow)
gl_npv_20_percent = npf.npv(interest_rates[1], gl_money_flow)

print(f'{gl_money_flow = }')
print(f'{gl_npv_10_percent = }')
print(f'{gl_npv_20_percent = }')

#Cast iron chlorinator:
ci_installed_cost = 7200
ci_life_estimate = 4
ci_salvage_value = 800
ci_annual_cost = ci_installed_cost*0.2
ci_yearly_premium = 0

ci_maintenence_cost = np.full(11,730)
ci_maintenence_cost[0] = 0

ci_money_flow = np.zeros(period)
ci_money_flow[0] -= ci_installed_cost

for i in range(1, len(ci_money_flow)):
    ci_money_flow[i] -= ci_annual_cost
    ci_money_flow[i] -= ci_maintenence_cost[i]
    if(i%4 == 0):
        ci_money_flow[i] += ci_salvage_value
        ci_money_flow[i] -= ci_installed_cost
#salvaging the chlorinator in year 10 even though it has more life
ci_money_flow[-1] += ci_salvage_value 

ci_npv_10_percent = npf.npv(interest_rates[0], ci_money_flow)
ci_npv_20_percent = npf.npv(interest_rates[1], ci_money_flow)

print(f'{ci_money_flow = }')
print(f'{ci_npv_10_percent = }')
print(f'{ci_npv_20_percent = }')