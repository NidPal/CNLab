import socket
name = input('Device name: ').strip() or 'Mobile1'
count = int(input('Messages to send [1]: ') or 1)
if not 1 <= count <= 100: raise ValueError('Choose 1-100 messages')
for i in range(count):
    msg = input(f'Message {i+1}: ')
    with socket.create_connection(('localhost', 5006)) as s:
        s.sendall(f'{name}: {msg}'.encode())
        print(s.recv(4096).decode())
