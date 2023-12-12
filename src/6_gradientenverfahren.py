import math
import matplotlib.pyplot as plt
import numpy as np


startPoints = [(2, 1), (0, 1), (-2, -2), (0,-2)]
epsilon = 0.5


def f(x, y):
    return -(x*y - 1)**2 * np.exp(-(x**2 + y**2)/2)

def fderivateX(x, y):
    return math.exp(-(x**2)/2-(y**2)/2) * (x**3*y**2-2*x**2*y-2*x*y**2+2*y)

def fderivateY(x, y):
    return math.exp(-(x**2)/2-(y**2)/2) * (x**2*y*(y**2-2)-2*x*(y**2-1)+y)


def gradient(x, y):
    return [
        fderivateX(x, y),
        fderivateY(x, y)
    ]

def gradientenverfahren(x, y, epsilon):
    i = 0
    x_values = [x]  # Store x values for plotting
    y_values = [y]  # Store y values for plotting
    while i < 100:
        grad = gradient(x, y)
        x = x - epsilon * grad[0]
        y = y - epsilon * grad[1]
        x_values.append(x)
        y_values.append(y)
        i += 1

    # Plot the trajectory for this starting point
    plt.plot(x_values, y_values, '-o', markersize=3, linewidth=1)
    return [x, y]



def main():
    for x, y in startPoints:
        print ("Startpunkt: " + str(x) + ", " + str(y))
        print(gradientenverfahren(x, y, epsilon))
        print("")

    x = np.linspace(-3.5, 3.5, 200)
    y = np.linspace(-3.5, 3.5, 200)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gradientenverfahren mit Startpunkten (2, 1), (0, 1), (-1, -1), (-2, -2)')
    plt.grid(True)
    plt.contourf(X, Y, Z, 100)
    plt.show()


if __name__ == "__main__":
    main()