import simpy

n = int(input('Number of frames [5]: ') or 5)
w = int(input('Window size [3]: ') or 3)
lost = int(input('Lost frame (-1 = none) [2]: ') or 2)
delay = float(input('Delay per frame [1]: ') or 1)
if not (1 <= n <= 1000 and 1 <= w <= n and -1 <= lost < n and delay > 0):
    raise ValueError('Invalid parameters')

def run(env):
    for start in range(0, n, w):
        end = min(start + w, n)
        print('Window:', list(range(start, end)))
        for f in range(start, end):
            print(env.now, 'Sent', f)
            yield env.timeout(delay)
            if f == lost:
                print(env.now, 'Lost', f)
            elif lost >= start and lost < end and f > lost:
                print(env.now, 'Discarded', f)
            else:
                print(env.now, 'ACK', f)
        if start <= lost < end:
            print('Timeout')
            for f in range(lost, end):
                print(env.now, 'Resent', f)
                yield env.timeout(delay)
                print(env.now, 'ACK', f)

env = simpy.Environment()
env.process(run(env))
env.run()
