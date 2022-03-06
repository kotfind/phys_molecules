import numpy as np
from copy import deepcopy

from Plane import Plane
from Ball import Ball
from Plot import plot3d, plot2d
from Random import rand_vec

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
        s.plot_speeds = 1

        # Create planes
        s.planes = []
        for i in range(3):
            for j in [1, 0]:
                pos = np.array([0] * 3)
                norm = np.array([0] * 3)
                norm[i] = 1 - 2 * j
                pos[i] = j
                s.planes.append(Plane(pos, norm))

        # Create balls
        s.balls = [Ball(s.ball_radius, np.array([0.5] * 3), rand_vec() * s.max_ball_speed) for i in range(s.balls_quantity)]

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

        if s.plot_speeds:
            s.speeds = [0] * 1000
            for ball in s.balls:
                s.speeds[int(ball.velocity[0] / s.max_ball_speed * 1000)] += 1;
            toplot = [[]]
            for i in range(1000):
                toplot[0].append((i / 1000 * s.max_ball_speed, s.speeds[i]))
            plot2d(toplot)

    def process_collsions(s, t):
        for i in range(len(s.planes)):
            plane = s.planes[i]
            momentum = 0
            for ball in s.balls:
                if ball.collides(plane):
                    momentum += abs(np.dot(ball.velocity, plane.norm))
                    ball.velocity = rand_vec() * np.linalg.norm(ball.velocity)
                    if np.dot(ball.velocity, plane.norm) < 0:
                        ball.velocity *= -1

            if s.plot_momentums:
                s.momentums[i].append(np.array([t, momentum]))
