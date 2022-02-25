import numpy as np
import matplotlib.pyplot as plt

def plot3d(lines):
    fig = plt.figure()

    for coords in lines:
        ax = plt.gca(projection = '3d')

        x = [coord[0] for coord in coords]
        y = [coord[1] for coord in coords]
        z = [coord[2] for coord in coords]

        ax.plot(x, y, z, color=np.random.rand(3,))

    plt.show()

def plot2d(lines):
    fig = plt.figure()

    for coords in lines:
        ax = fig.gca()

        x = [coord[0] for coord in coords]
        y = [coord[1] for coord in coords]

        ax.plot(x, y, color=np.random.rand(3,))

    plt.show()
