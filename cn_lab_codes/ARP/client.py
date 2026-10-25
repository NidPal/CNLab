import socket
while True:
    ip = input('IP to resolve (blank to quit): ').strip()
    if not ip: break
    with socket.create_connection(('localhost', 5001)) as s:
        s.sendall(ip.encode())
        print('MAC:', s.recv(4096).decode())
