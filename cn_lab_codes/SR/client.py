import socket

n = int(input('Number of frames [5]: ') or 5)
w = int(input('Window size [3]: ') or 3)
lost = int(input('Frame to lose (-1 for none) [2]: ') or 2)
if not (1 <= n <= 1000 and 1 <= w <= n and -1 <= lost < n):
    raise ValueError('Require 1 <= window <= frames <= 1000 and -1 <= lost < frames')
with socket.create_connection(('localhost', 5003)) as s:
    s.sendall(f'{n},{w},{lost}'.encode())
    s.shutdown(socket.SHUT_WR)
    print(''.join(iter(lambda: s.recv(4096).decode(), '')))
