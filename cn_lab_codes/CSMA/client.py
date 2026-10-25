import socket
msg = input('Message: ')
with socket.create_connection(('localhost', 5004)) as s:
    s.sendall(msg.encode())
    print(s.recv(4096).decode())
