from pygem import RBFParameters, RBF
import numpy as np
import matplotlib.pyplot as plt

# read the RBF parameters
params = RBFParameters()
params.read_parameters(
    filename='cartesian_test.prm')

nx, ny, nz = (50, 10, 10)
mesh = np.zeros((nx * ny * nz, 3))

xv = np.linspace(0, 5, nx)
yv = np.linspace(0, 1, ny)
zv = np.linspace(0, 1, nz)

# vectors
z, y, x = np.meshgrid(zv, yv, xv)

mesh = np.array([x.ravel(), y.ravel(), z.ravel()])
mesh = mesh.T

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(mesh[:, 0], mesh[:, 1], mesh[:, 2], c='blue', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()

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
