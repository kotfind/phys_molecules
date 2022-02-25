import numpy as np
from copy import deepcopy

from Plane import Plane
from Ball import Ball
from Plot import plot3d, plot2d

class Engine:
    def __init__(s):
        # Options
        s.max_time = 1
        s.delta_time = 1e-2
        s.max_ball_speed = 1e2;
        s.ball_radius = 1e-2;
        s.balls_quantity = int(5e3)
        s.plot_coords = 0
        s.plot_momentums = 1

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
        s.balls = [Ball(s.ball_radius, np.random.rand(3,), (np.random.rand(3,) - 0.5) * 2) for i in range(s.balls_quantity)]

    def run(s):
        t = 0

        if s.plot_coords:
            s.coords = [[] for i in range(len(s.balls))]
        if s.plot_momentums:
            s.momentums = [[] for i in range(len(s.planes))]

        while t < s.max_time:
            s.process_collsions(t)
            for i in range(len(s.balls)):
                ball = s.balls[i]
                ball.move(s.delta_time)
                if s.plot_coords:
                    s.coords[i].append(deepcopy(ball.pos))
            t += s.delta_time

        if s.plot_coords:
            plot3d(s.coords)

        if s.plot_momentums:
            plot2d(s.momentums)

    def process_collsions(s, t):
        for i in range(len(s.planes)):
            plane = s.planes[i]
            momentum = 0
            for ball in s.balls:
                if ball.collides(plane):
                    ball.reflect(plane.norm)
                    momentum += abs(np.dot(ball.velocity, plane.norm))

            if s.plot_momentums:
                s.momentums[i].append(np.array([t, momentum]))
