import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot()

# from 0 to 10, with 100 steps
s = np.linspace(-10, 10, 100)
t = np.linspace(-10, 10, 100)
s, t = np.meshgrid(s, t)

x = s
y = t
z = (-3) * (-2*s) - t

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Parametrisierte Ebene in R3")
ax.plot_surface(x, y, z)
plt.show()