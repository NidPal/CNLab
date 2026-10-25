import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5003))
s.listen()
print('Listening on 5003 (Ctrl+C to stop)')
while True:
    c, addr = s.accept()
    with c:
        try:
            n, w, lost = map(int, c.recv(1024).decode().split(','))
            if not (1 <= n <= 1000 and 1 <= w <= n and -1 <= lost < n):
                raise ValueError('Invalid frame/window/loss parameters')
            lines = [f'Frames={n}, window={w}, lost={lost}']
            for start in range(0, n, w):
                frames = range(start, min(start + w, n))
                lines.append(f'Window: {list(frames)}')
                for f in frames:
                    if f == lost:
                        lines.append(f'Frame {f} lost')
                    elif False:
                        lines.append(f'Frame {f} discarded (GBN)')
                    else:
                        lines.append(f'ACK {f}')
                if lost in frames:
                    lines.append(f"Timeout: resend only frame {lost}")
                    for f in [lost]:
                        lines.append(f'Resent {f} -> ACK {f}')
            c.sendall(('\n'.join(lines) + '\n').encode())
        except (ValueError, OSError) as e:
            c.sendall(('Error: ' + str(e)).encode())
