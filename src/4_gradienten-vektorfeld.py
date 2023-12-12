import numpy as np
import matplotlib.pyplot as plt

# Gitter Definition
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Sehr kleine Werte werden bei x und y = 0 eingesetzt
X[X == 0] = 1e-10
Y[Y == 0] = 1e-10

# Berechnung der Gradienten
U1 = Y / (X**2 + Y**2)**(3/2)
V1 = X / (X**2 + Y**2)**(3/2)

U2 = -Y / (X**2 + Y**2)**(3/2)
V2 = -X / (X**2 + Y**2)**(3/2)

# Plot
plt.figure(figsize=(12, 6))

# Normale 1
plt.subplot(1, 2, 1)
plt.quiver(X, Y, U1, V1, color='blue')
plt.title('Normale 1')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x')
plt.ylabel('y')

# Normale 2
plt.subplot(1, 2, 2)
plt.quiver(X, Y, U2, V2, color='green')
plt.title('Normale 2')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
