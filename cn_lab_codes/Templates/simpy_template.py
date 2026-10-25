import simpy
def process(env):
    print('Start:', env.now)
    yield env.timeout(2)
    print('End:', env.now)
env = simpy.Environment()
env.process(process(env))
env.run()
