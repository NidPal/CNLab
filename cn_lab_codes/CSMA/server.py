import socket
import threading
import time
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5004))
s.listen()
lock = threading.Lock()
def handle(c):
    try:
        msg = c.recv(1024).decode()
        if lock.acquire(blocking=False):
            try:
                c.sendall(b'Channel Free: Transmitting')
                print('Transmitting:', msg)
                time.sleep(2)
            finally:
                lock.release()
        else:
            c.sendall(b'Channel Busy: Try Again')
    finally:
        c.close()
while True:
    c, addr = s.accept()
    threading.Thread(target=handle, args=(c,), daemon=True).start()
