# autopep8 --in-place --aggressive .\move_airfoil.py
from pygem import RBFParameters, RBF
import numpy as np
import matplotlib.pyplot as plt

# original 2-D mesh
# read the mesh file
file = open("n0012_50.dat", "r")
aux = file.readline()
nx, ny, nz = aux.split()
nx = int(nx)
ny = int(ny)
nz = int(nz)
mesh = np.zeros((nx * ny * nz, 3))

i = 0
for line in file:
    x, y, z = line.split()
    mesh[i] = [float(x), float(y), float(z)]
    i += 1
#
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(mesh[:, 0], mesh[:, 1], mesh[:, 2], c='blue', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()

# modified 2-D mesh

# read the RBF parameters
params = RBFParameters()
params.read_parameters(
    filename='turn_airfoil.prm')

params.plot_points()

params.save_points(filename='point.vtk')
#
rbf = RBF(params, mesh)
rbf.perform()
new_mesh_points = rbf.modified_mesh_points
#

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(new_mesh_points[:, 0], new_mesh_points[:, 1],
           new_mesh_points[:, 2], c='red', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
