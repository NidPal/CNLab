import simpy
n = int(input('Stations [3]: ') or 3)
tx = float(input('Transmission duration [2]: ') or 2)
if not (1 <= n <= 100 and tx > 0): raise ValueError('Invalid parameters')
def station(env, name, channel):
    print(name, 'checking channel')
    with channel.request() as req:
        yield req
        print(name, 'transmitting at', env.now)
        yield env.timeout(tx)
        print(name, 'finished at', env.now)
env = simpy.Environment()
channel = simpy.Resource(env, capacity=1)
for i in range(n): env.process(station(env, 'Station'+str(i+1), channel))
env.run()
