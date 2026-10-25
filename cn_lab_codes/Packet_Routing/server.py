import socket
import heapq
graph = {'A': {'B': 2, 'C': 4}, 'B': {'C': 1, 'D': 5}, 'C': {'D': 2}, 'D': {}}
def shortest(src, dst):
    q = [(0, src, [src])]
    while q:
        cost, node, path = heapq.heappop(q)
        if node == dst:
            return cost, path
        for nxt, weight in graph.get(node, {}).items():
            if nxt not in path:
                heapq.heappush(q, (cost + weight, nxt, path + [nxt]))
    return None
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5005))
s.listen()
while True:
    c, addr = s.accept()
    src, dst = c.recv(1024).decode().split()
    c.sendall(str(shortest(src, dst)).encode())
    c.close()
