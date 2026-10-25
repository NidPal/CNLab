import socket
s = socket.socket()
s.bind(('localhost', 5010))
s.listen()
while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    result = data.upper()  # Replace with core logic
    c.sendall(result.encode())
    c.close()
