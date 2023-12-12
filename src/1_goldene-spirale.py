import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot()

# from 0 to 10, with 100 steps
phi = np.linspace(0, 10, 100)

r = ((1 + np.sqrt(5)) / 2)**((2*phi) / np.pi)
x = r * np.cos(phi)
y = r * np.sin(phi)

ax.plot(x, y)
ax.legend()
ax.axes.set_xlabel("x")
ax.axes.set_ylabel("y")
ax.set_title("Goldene Spirale")
plt.show()