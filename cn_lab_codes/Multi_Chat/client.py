import socket
import threading

name = input('Username: ').strip() or 'Anonymous'
s = socket.create_connection(('localhost', 5000))

def receive():
    while True:
        try:
            msg = s.recv(1024)
            if not msg:
                break
            print(msg.decode(), end='')
        except OSError:
            break

threading.Thread(target=receive, daemon=True).start()
print('Type messages; exit to leave')
try:
    while True:
        msg = input('Message: ')
        if msg.lower() == 'exit':
            break
        if msg:
            s.sendall(f'{name}: {msg}\n'.encode())
finally:
    s.close()
