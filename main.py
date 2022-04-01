#!/bin/python3

from sys import argv
import pickle

from Engine import Engine

if __name__ == '__main__':
    try:
        if '-i' in argv:
            if '-o' in argv:
                print('-o and -i should not be used toogether')
                exit(1)

            filename = argv[argv.index('-i') + 1]
            with open(filename, 'rb') as file:
                engine = pickle.load(file)
            print('Loaded %s' % filename)
            print()
            engine.print_options()

        else:
            engine = Engine()

            engine.parse_arguments(argv)
            engine.print_options()

            engine.build_scene()
            engine.run()

        if '-o' in argv:
            filename = argv[argv.index('-o') + 1]
            with open(filename, 'wb') as file:
                pickle.dump(engine, file)
            print('Saved as %s' % filename)
            print()

        engine.plot()
        input()

    except KeyboardInterrupt:
        pass
