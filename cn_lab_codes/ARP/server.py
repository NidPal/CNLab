import socket
arp = {'192.168.1.1': 'AA:BB:CC:11', '192.168.1.2': 'AA:BB:CC:22', '192.168.1.3': 'AA:BB:CC:33'}
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5001))
s.listen()
while True:
    c, addr = s.accept()
    ip = c.recv(1024).decode()
    c.sendall(arp.get(ip, 'Not Found').encode())
    c.close()
