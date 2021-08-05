import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib
import numpy as np

# open in seperat window
matplotlib.use('tkagg')

# rosenbrock coefficients from wikipedia
a = 1
b = 100

# set up a meshgrid
x = y = np.arange(0, 10, 0.01)
X, Y = np.meshgrid(x, y)

# Rosenbrock function values
Z = (a-X**2)**2 + b*(Y-X)**2
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, )

# TODO: add newton method and steepest gradient method
# by adding each solution to the meshgrid

# to show and keep the plots in place before exiting
plt.show()
input('Press enter to exit')