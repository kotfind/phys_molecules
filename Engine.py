import numpy as np
from copy import deepcopy
from math import *
from time import process_time

from Plane import Plane
from Ball import Ball
from Plot import plot
from Random import rand_unit_vec, rand_vec

class Engine:
    def __init__(s):
        # Default Options
        s.max_time = 3
        s.delta_time = 1e-2
        s.min_ball_speed = 1e1;
        s.max_ball_speed = 1e2;
        s.ball_radius = 1e-10;
        s.balls_quantity = int(5e3)
        s.speed_bins = int(3e2)
        s.plot_momentums = 0
        s.plot_speeds = 0

    def parse_arguments(s, argv):
        if '-t' in argv:
            s.max_time = float(argv[argv.index('-t') + 1])

        if '-d' in argv:
            s.delta_time = float(argv[argv.index('-d') + 1])

        if '--min-ball-speed' in argv:
            s.min_ball_speed = float(argv[argv.index('--min-ball-speed') + 1])

        if '--max-ball-speed' in argv:
            s.max_ball_speed = float(argv[argv.index('--max-ball-speed') + 1])

        if '-r' in argv:
            s.ball_radius = float(argv[argv.index('-r') + 1])

        if '-n' in argv:
            s.balls_quantity = int(argv[argv.index('-n') + 1])

        if '-b' in argv:
            s.speed_bins = int(argv[argv.index('-b') + 1])

        if '-m' in argv:
            s.plot_momentums = 1

        if '-s' in argv:
            s.plot_speeds = 1

    def print_options(s):
        print('Using current options:')
        print('Max time:       %.5f' % s.max_time)
        print('Delta time:     %.5f' % s.delta_time)
        print('Min ball speed: %.5f' % s.min_ball_speed)
        print('Max ball speed: %.5f' % s.max_ball_speed)
        print('Ball raduius:   %.5f' % s.ball_radius)
        print('Balls quantity: %d'   % s.balls_quantity)
        print('Speed bins:     %d'   % s.speed_bins)
        print('Plot momentums: %d'   % s.plot_momentums)
        print('Plot speeds:    %d'   % s.plot_speeds)
        print()

    def build_scene(s):
        # Create planes
        s.planes = Plane.cube()

        # Create balls
        s.balls = [Ball(s.ball_radius, np.array([0.5] * 3), rand_vec(s.min_ball_speed, s.max_ball_speed)) for i in range(s.balls_quantity)]

    def run(s):
        start_time = process_time()

        frames = ceil(s.max_time / s.delta_time)
        for frame in range(frames):
            time = frame * s.delta_time
            for ball in s.balls:
                for plane in s.planes:
                    s.process_collision(ball, plane)
                ball.move(s.delta_time)
            for plane in s.planes:
                plane.fix_momentum(time)

        print("Processed in %.3f seconds" % (process_time() - start_time))

    def plot(s):
        if s.plot_momentums:
            plot([plane.momentums for plane in s.planes],
                colours=[(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)],
                labels=["pos: %10s; norm: %10s" %
                    (np.array2string(plane.pos), np.array2string(plane.norm))
                        for plane in s.planes],
                title='Momentum distribution',
                xlabel='Time',
                ylabel='Momentum')

        if s.plot_speeds:
            plot([([abs(ball.velocity[coord_idx])
                    for ball in s.balls], s.speed_bins)
                        for coord_idx in range(3)],
                mode='hist',
                colours=['r', 'g', 'b'],
                labels=['x', 'y', 'z'],
                title='Speed distribution',
                xlabel='Speed',
                ylabel='Quantity')

    def process_collision(s, ball, plane):
        d = np.dot(ball.pos, plane.norm) - np.dot(plane.pos, plane.norm) - ball.radius
        if d < 0:
            ball.pos -= plane.norm * d
            plane.add_momentum(abs(np.dot(ball.velocity, plane.norm)))
            ball.velocity = rand_unit_vec() * np.linalg.norm(ball.velocity)
            if np.dot(ball.velocity, plane.norm) < 0:
                ball.velocity *= -1
