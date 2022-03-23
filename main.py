from Engine import Engine

if __name__ == '__main__':
    try:
        engine = Engine()
        engine.build_scene()
        engine.run()
        engine.plot()
        input()
    except KeyboardInterrupt:
        pass
