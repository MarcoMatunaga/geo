# autopep8
# autopep8 --in-place --aggressive .\meshgrid_test.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2-D mesh
nx, ny = (10, 10)
xv = np.linspace(0, 3, nx)
yv = np.linspace(0, 1, ny)
x, y = np.meshgrid(xv, yv)

mesh = np.array([x.ravel(), y.ravel()])
mesh = mesh.T

fig1 = plt.figure(1)
ax = fig1.add_subplot(111)
ax.scatter(mesh[:, 0], mesh[:, 1], c='blue', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
plt.show()

# 3-D mesh
nx, ny, nz = (10, 10, 1)
xv = np.linspace(0, 3, nx)
yv = np.linspace(0, 1, ny)
zv = np.linspace(0, 0, nz)
x, y, z = np.meshgrid(xv, yv, zv)

mesh = np.array([x.ravel(), y.ravel(), z.ravel()])
mesh = mesh.T

fig2 = plt.figure(2)
ax1 = fig2.add_subplot(111, projection='3d')
ax1.scatter(mesh[:, 0], mesh[:, 1], mesh[:, 2], c='blue', marker='o')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
plt.show()
