#!/bin/python3

from Engine import Engine
import sys

if __name__ == '__main__':
    try:
        engine = Engine()

        engine.parse_arguments(sys.argv)
        engine.print_options()

        engine.build_scene()
        engine.run()

        engine.plot()
        input()

    except KeyboardInterrupt:
        pass
