import simpy
n = int(input('Devices [3]: ') or 3)
packets = int(input('Packets per device [1]: ') or 1)
delay = float(input('Transmission delay [2]: ') or 2)
if not (1 <= n <= 100 and 1 <= packets <= 100 and delay > 0): raise ValueError('Invalid parameters')
def device(env, name, channel):
    for p in range(1, packets+1):
        with channel.request() as req:
            yield req
            print(env.now, name, 'sending packet', p)
            yield env.timeout(delay)
            print(env.now, 'AP received packet', p, 'from', name)
env = simpy.Environment()
channel = simpy.Resource(env, capacity=1)
for i in range(n): env.process(device(env, 'Mobile'+str(i+1), channel))
env.run()
