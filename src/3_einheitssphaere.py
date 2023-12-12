import matplotlib.pyplot as plt
import numpy as np


# from 0 to 2*pi, with 1000 steps
phi = np.linspace(0, 2*np.pi, 20)
# from 0 to pi, with 1000 steps
theta = np.linspace(0, np.pi, 20)
phi, theta = np.meshgrid(phi, theta)

# calculate x, y, z- coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Plotten der Einheitssphäre in 3D
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Einheitssphäre")
ax.plot_surface(x, y, z, alpha=0.6)

plt.show()
