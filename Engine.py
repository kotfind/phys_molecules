import numpy as np
from copy import deepcopy

from Plane import Plane
from Ball import Ball
from Plot import plot3d

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
        s.balls = [Ball(np.random.rand(3,), np.random.rand(3,) * 2 - 1) for i in range(int(5e3))]

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
        plot3d(coords)

    def process_collsions(s):
        for plane in s.planes:
            for ball in s.balls:
                if ball.collides(plane):
                    ball.reflect(plane.norm)
