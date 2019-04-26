# autopep8 --in-place --aggressive .\pygem_airfoil.py
from pygem import RBFParameters, RBF
import numpy as np
import matplotlib.pyplot as plt

# original 2-D mesh
# read the mesh file
file = open("mesh", "r")
aux = file.readline()
nx, ny, nz = aux.split()
nx = int(nx)
ny = int(ny)
nz = int(nz)
mesh = np.zeros((nx * ny * nz, 3))

i = 0
for line in file:
    x,y,z = line.split()
    mesh[i] = [float(x),float(y),float(z)]
    i += 1
#
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(mesh[:, 0], mesh[:, 1], mesh[:, 2], c='blue', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
#
# modified 2-D mesh
#
