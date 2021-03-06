import numpy as np

y = np.matrix([[120.2], [95.2], [180], [142.8], [35.7], [80.2]])

V = np.matrix([
    [1.2, 0, 0, 0, 0, 0],
    [0, 0.5, 0, 0, 0, 0],
    [0, 0, 5.0, 0, 0, 0],
    [0, 0, 0, 0.8, 0, 0],
    [0, 0, 0, 0, 0.5, 0],
    [0, 0, 0, 0, 0, 0.2],
])

A = np.matrix([
    [1, 0, -1, 1, 0, -1],
    [0, 0, 1, -1, -1, 0],
])

ŷ = y-V*(A.T)*np.linalg.inv(A*V*(A.T))*A*y

print(f'{ŷ = }')