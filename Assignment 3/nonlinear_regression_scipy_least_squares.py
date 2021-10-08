import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def model(B, x):
    return B[0]+B[1]*np.exp(-B[2]*x)

def fun(B, x, y):
    return model(B, x) - y

# measurements
xm = np.array([0.0,0.0,1.0,1.0,2.0,2.0,3.0,3.0,4.0,4.0,5.0,5.0])
ym = np.array([2.86,2.64,1.57,1.24,0.45,1.02,0.65,0.18,0.15,0.01,0.04,0.36])

#initial guess
B0 = np.array([1,1,1])

res = least_squares(fun, B0, bounds=(0, 100), args=(xm, ym), verbose=1)

print(res)

print(f'Optimized B1 = {res.x[0]}')
print(f'Optimized B2 = {res.x[1]}')
print(f'Optimized B3 = {res.x[2]}')

#x_modelled = np.linspace(0, 5)
y_modelled = model(res.x, xm)
plt.plot(xm, ym, 'o', markersize=4, label='data')
plt.plot(xm, y_modelled, label='fitted model')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='best')
plt.show()