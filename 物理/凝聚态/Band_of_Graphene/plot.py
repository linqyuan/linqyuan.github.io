import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

kx = np.linspace(-2*np.pi/3, 2*np.pi/3, 800)
ky = np.linspace(-2*np.pi/3, 2*np.pi/3, 800)
kx, ky = np.meshgrid(kx, ky)
Ek = np.sqrt(3 + 4*np.cos(1.5*kx)*np.cos(np.sqrt(3)/2*ky) + 2*np.cos(np.sqrt(3)*ky))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(kx, ky, Ek, rstride=1, cstride=1, cmap='rainbow')
ax.plot_surface(kx, ky, -Ek, rstride=1, cstride=1, cmap='rainbow')
plt.xlabel('kx')
plt.ylabel('ky')
plt.show()
