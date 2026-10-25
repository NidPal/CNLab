import socket
s = socket.socket()
s.connect(('localhost', 5010))
data = input('Enter data: ')
s.sendall(data.encode())
print(s.recv(1024).decode())
s.close()
