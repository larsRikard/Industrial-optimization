from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

# measurements
xm = np.array([0.0,0.0,1.0,1.0,2.0,2.0,3.0,3.0,4.0,4.0,5.0,5.0])
ym = np.array([2.86,2.64,1.57,1.24,0.45,1.02,0.65,0.18,0.15,0.01,0.04,0.36])


# GEKKO model
m = GEKKO(remote=False)

# parameters
x = m.Param(value=xm)
B1 = m.FV()
B1.STATUS=1
B2 = m.FV()
B2.STATUS=1
B3 = m.FV()
B3.STATUS=1

# variables
y = m.CV(value=ym)
y.FSTATUS=1

# regression equation
m.Equation(y==B1+B2*m.exp(-B3*x))

# regression mode
m.options.IMODE = 2

# optimize
m.solve(disp=True)

# print parameters
print(f'Optimized B1 = {B1[0]}')
print(f'Optimized B2 = {B2[0]}')
print(f'Optimized B3 = {B3[0]}')

plt.figure(1)
plt.plot(xm,ym,'bo')
plt.plot(xm,y.value,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Measured','Model'],loc='best')
plt.show()