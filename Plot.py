import numpy as np
import matplotlib.pyplot as plt

def plot(lines, plot_3d=False, colours=None, labels=None,
        title='', xlabel='', ylabel='', zlabel=''):
    fig = plt.figure()
    fig.canvas.set_window_title('doFloat')

    for line_idx, line in enumerate(lines):
        ax = plt.gca(projection = ('3d' if plot_3d else None))

        ax.grid(linestyle='--', linewidth=0.5)
        ax.set_title(title)
        ax.set_xlabel(xlabel, loc='right')
        ax.set_ylabel(ylabel, loc='top')
        if plot_3d:
            ax.set_zlabel(zlabel)

        x = [coord[0] for coord in line]
        y = [coord[1] for coord in line]
        z = [coord[2] for coord in line] if plot_3d else None

        colour = colours[line_idx] if colours else np.random.rand(3,)
        label = labels[line_idx] if labels else ''

        if plot_3d:
            ax.plot(x, y, z, color=colour, label=label)
        else:
            ax.plot(x, y, color=colour, label=label)

    if labels:
        plt.legend()
    plt.ion()
    plt.show()
