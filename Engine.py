import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

from Plane import Plane
from Ball import Ball

class Engine:
    def __init__(s):
        # Create planes
        s.planes = []
        for i in range(3):
            for j in [1, 0]:
                pos = np.array([0] * 3)
                norm = np.array([0] * 3)
                norm[i] = 1
                pos[i] = j
                s.planes.append(Plane(pos, norm))

        # Create balls
        s.balls = [Ball(np.random.rand(3,), np.random.rand(3,)) for i in range(10)]

    def run(s, time, dtime):
        t = 0
        coords = [[] for i in range(len(s.balls))]
        while t < time:
            s.process_collsions()
            for i in range(len(s.balls)):
                ball = s.balls[i]
                ball.move(dtime)
                coords[i].append(deepcopy(ball.pos))
            t += dtime
        s.plot(coords)

    def process_collsions(s):
        for plane in s.planes:
            for ball in s.balls:
                if ball.collides(plane):
                    ball.reflect(plane.norm)
                    
    def plot(s, arr):
        fig = plt.figure()

        for coords in arr:
            ax = plt.gca(projection = '3d')

            x = [coord[0] for coord in coords]
            y = [coord[1] for coord in coords]
            z = [coord[2] for coord in coords]

            ax.plot(x, y, z, color=np.random.rand(3,))

        plt.show()
