# autopep8 --in-place --aggressive .\control_points_rbf.py
import numpy as np
import re
import math

alpha = input("Choose the turn angle (degrees) for the airfoil:")
alpha = float(alpha)*(180.0/math.pi)
# file with the RBF parameters
f_control_points = open("turn_airfoil.prm", "w")

"""
choose the radial basis function
there are several see the package reference
to see more about each one
"""
# let work with gaussian spline
header = "[Radial Basis Functions] \n"
f_control_points.write(header)

# The chosen RBF function
f_control_points.write("basis function: ")
rbf_function = "gaussian_spline \n"
f_control_points.write(rbf_function)

# the arguments for the radial basis function
"""
in this case only took two
radius and power
"""
radius = 0.5
arg = "radius: "
f_control_points.write(("%s %f") % (arg, radius))
f_control_points.write("\n")

# arg
power = 2
arg = "power: "
f_control_points.write(("%s %i") % (arg, power))
f_control_points.write("\n")

# original 2-D mesh
# read the mesh file
file = open("n0012_50.dat", "r")
aux = file.readline()
nx, ny, nz = aux.split()
nx = int(nx)
ny = int(ny)
nz = int(nz)

# define the mesh size and put zeros on it
mesh = np.zeros((nx * ny * nz, 3))

#
str = "[Control points]\n"
f_control_points.write(str)
str = "original control points: "
f_control_points.write(str)
i = 0
for line in file:
    # the control points are the airfoil points
    x, y, z = line.split()
    f_control_points.write(("%f %f %f \n") % (float(x), float(y), float(z)))
    f_control_points.write(len(str) * " ")
    #
    mesh[i] = [float(x), float(y), float(z)]
    i += 1

f_control_points.write("\n")
f_control_points.write("deformed control points: ")

"""
Calculate the modified control points for the airfoil
The last pont does not change coordinates
"""
xd = mesh[0][0]
yd = mesh[0][1]
zd = mesh[0][2]
f_control_points.write(("%f %f %f\n") % (xd, yd, zd))
f_control_points.write(len(str) * " ")

for i in range(1, nx * ny * nz, 1):
    # xl is the airfoil x-coordinate
    xl = mesh[i][0]
    xd = xl * math.cos(alpha)
    yd = xl * math.sin(alpha)
    zd = mesh[i][2]

    xd = xd + mesh[i][1] * math.sin(alpha / 2)
    yd = yd + mesh[i][1] * math.cos(alpha / 2)
    f_control_points.write(("%f %f %f\n") % (xd, yd, zd))
    f_control_points.write(len(str) * " ")

# print(alpha)
