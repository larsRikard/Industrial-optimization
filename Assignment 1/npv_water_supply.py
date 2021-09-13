import numpy as np
import numpy_financial as npf
import scipy.optimize as spo
# Problem 3.13

#Common:
interest_rate = 0.12

#Plan A:
pipeline_A = 160_000 #$
annual_operation_and_upkeep_A = 2200 #$
lifetime_A = 31 #years

#* Money flow A
money_flow_A = np.zeros(lifetime_A)
money_flow_A[0] += -pipeline_A
for i in range(1,lifetime_A):
    money_flow_A[i] += -annual_operation_and_upkeep_A
print(f'{money_flow_A = }')

#Plan B
flume_B = 34_000 #$
flume_lifetime_B = 10 #years
flume_B_salvage_value = 5600 #$
annual_operation_flume_B = 4500 #$
ditch_B = 58_000 #$
annual_ditch_B_upkeep = 2500 #$
lifetime_B = 31 #years

#* Money flow B
money_flow_B = np.zeros(lifetime_B)
# year 0 investments
money_flow_B[0] += -flume_B
money_flow_B[0] += -ditch_B
#from year 1 and even year 30
for i in range(1,lifetime_B):
    money_flow_B[i] += -annual_operation_flume_B
    money_flow_B[i] += -annual_ditch_B_upkeep
    #last year we don't buy a new flume
    if(i%30 == 0):
        money_flow_B[i] += flume_B_salvage_value
    #every 10th year we salvage and buy new flume
    elif(i%10 == 0):
        print(i)
        money_flow_B[i] += flume_B_salvage_value
        money_flow_B[i] += -flume_B

print(f'{money_flow_B = }')


npv_A = npf.npv(interest_rate,money_flow_A)
npv_B = npf.npv(interest_rate,money_flow_B)

print(f'{npv_A = }')
print(f'{npv_B = }')