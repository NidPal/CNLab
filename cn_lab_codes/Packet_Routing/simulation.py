import simpy
import heapq
graph = {'A': {'B': 2, 'C': 4}, 'B': {'C': 1, 'D': 5}, 'C': {'D': 2}, 'D': {}}
src = (input('Source [A]: ') or 'A').upper()
dst = (input('Destination [D]: ') or 'D').upper()
q = [(0, src, [src])]
answer = None
while q:
    cost, node, path = heapq.heappop(q)
    if node == dst:
        answer = (cost, path)
        break
    for nxt, weight in graph.get(node, {}).items():
        if nxt not in path: heapq.heappush(q, (cost+weight, nxt, path+[nxt]))
if answer is None:
    print('No route found')
else:
    print('Shortest path:', answer)
    def routing(env, path):
        print(env.now, 'Packet at', path[0])
        for a, b in zip(path, path[1:]):
            yield env.timeout(graph[a][b])
            print(env.now, 'Packet at', b)
    env = simpy.Environment()
    env.process(routing(env, answer[1]))
    env.run()
