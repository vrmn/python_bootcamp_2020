from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

u=np.linspace(0,2*np.pi,100)
v=np.linspace(0,2*np.pi,100)
u,v=np.meshgrid(u,v)
a = 6
b = 5
X = (b + a*np.cos(u)) * np.cos(v)
Y = (b + a*np.cos(u)) * np.sin(v)
Z = a * np.sin(u)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
#ax.set_aspect('equal')

ax.scatter([0,0], [0,0], [-3,3], c='r', marker='o')
ax.plot_surface(X, Y, Z,alpha=0.05, cmap='viridis', edgecolor='black')
ax.scatter([0,0], [0,0], [-3,3], c='r', marker='o')

plt.show()
