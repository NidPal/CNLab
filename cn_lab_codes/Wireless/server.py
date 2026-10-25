import socket
import threading
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5006))
s.listen()
def handle(c):
    try:
        msg = c.recv(1024).decode()
        print('Received:', msg)
        c.sendall(('AP received: ' + msg).encode())
    finally:
        c.close()
while True:
    c, addr = s.accept()
    threading.Thread(target=handle, args=(c,), daemon=True).start()
