import simpy
n = int(input('Number of clients [3]: ') or 3)
count = int(input('Messages per client [3]: ') or 3)
delay = float(input('Interval [1]: ') or 1)
if not (1 <= n <= 100 and 1 <= count <= 100 and delay > 0): raise ValueError('Invalid parameters')
def chat(env, name):
    for i in range(count):
        print(env.now, name, 'sends message', i + 1)
        yield env.timeout(delay)
env = simpy.Environment()
for i in range(n): env.process(chat(env, 'Client ' + str(i+1)))
env.run()
