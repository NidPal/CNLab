import socket
src = (input('Source [A]: ') or 'A').upper()
dst = (input('Destination [D]: ') or 'D').upper()
with socket.create_connection(('localhost', 5005)) as s:
    s.sendall(f'{src} {dst}'.encode())
    print('Shortest Route:', s.recv(4096).decode())
