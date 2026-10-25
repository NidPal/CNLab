import socket
import threading

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5000))
s.listen()
clients = []
lock = threading.Lock()

def handle(c):
    try:
        while True:
            msg = c.recv(1024)
            if not msg:
                break
            with lock:
                others = [x for x in clients if x != c]
            for x in others:
                try:
                    x.sendall(msg)
                except OSError:
                    pass
    finally:
        with lock:
            if c in clients:
                clients.remove(c)
        c.close()

while True:
    c, addr = s.accept()
    with lock:
        clients.append(c)
    threading.Thread(target=handle, args=(c,), daemon=True).start()
