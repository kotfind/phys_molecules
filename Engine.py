import numpy as np
from copy import deepcopy
from math import *

from Plane import Plane
from Ball import Ball
from Plot import plot3d, plot2d
from Random import rand_vec

class Engine:
    def __init__(s):
        # Options
        s.max_time = 3
        s.delta_time = 1e-2
        s.max_ball_speed = 1;
        s.ball_radius = 1e-10;
        s.balls_quantity = int(5e3)
        s.delta_ball_speed = 1e-3
        s.plot_coords = 0
        s.plot_momentums = 0
        s.plot_speeds = 1

        # Create planes
        s.planes = Plane.cube()

        # Create balls
        s.balls = [Ball(s.ball_radius, np.array([0.5] * 3), rand_vec() * s.max_ball_speed) for i in range(s.balls_quantity)]

    def run(s):
        frame = 0

        frames = ceil(s.max_time / s.delta_time)
        for frame in range(frames):
            time = frame * s.delta_time
            for ball in s.balls:
                for plane in s.planes:
                    s.process_collision(ball, plane)
                ball.fix_coords()
                ball.move(s.delta_time)
            for plane in s.planes:
                plane.fix_momentum(time)

        if s.plot_coords:
            plot3d([ball.traectory for ball in s.balls])

        if s.plot_momentums:
            plot2d([plane.momentums for plane in s.planes])

        if s.plot_speeds:
            plot2d([Ball.get_speeds(s.balls, s.max_ball_speed, s.delta_ball_speed)])

    def process_collision(s, ball, plane):
        d = np.dot(ball.pos, plane.norm) - np.dot(plane.pos, plane.norm) - ball.radius
        if d < 0:
            ball.pos -= plane.norm * d
            plane.add_momentum(abs(np.dot(ball.velocity, plane.norm)))
            ball.velocity = rand_vec() * np.linalg.norm(ball.velocity)
            if np.dot(ball.velocity, plane.norm) < 0:
                ball.velocity *= -1
