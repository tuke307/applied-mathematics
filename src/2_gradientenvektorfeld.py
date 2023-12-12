import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot()

# Erstellen eines Gitters von Werten in R^2 \ {0}
# from -10 to 10, with 40 steps
x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
X, Y = np.meshgrid(x, y)

# Berechnen der euklidischen Norm
r = 1 / np.sqrt(X**2 + Y**2)

# Berechnen der Gradientenkomponenten des Vektorfeldes
norm_x = r * (-Y)
norm_y = r * X

# Plotten der Normalen
plt.figure(figsize=(7, 7))
plt.quiver(X, Y, norm_x, norm_y, scale=50, color="b")  # Um Verktorfelder zu zeichnen
plt.title(
    "Normalen zum Gradientenvektorfeld der euklidischen Norm"
)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.show()



