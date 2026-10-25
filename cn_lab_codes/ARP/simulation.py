import simpy
arp = {'192.168.1.1': 'AA:BB:CC:11', '192.168.1.2': 'AA:BB:CC:22'}
ip = input('IP to resolve [192.168.1.1]: ') or '192.168.1.1'
delay = float(input('Reply delay [2]: ') or 2)
if delay < 0: raise ValueError('Delay must be nonnegative')
def process(env):
    print(env.now, 'ARP Request:', ip)
    yield env.timeout(delay)
    print(env.now, 'ARP Reply:', arp.get(ip, 'Not Found'))
env = simpy.Environment()
env.process(process(env))
env.run()
