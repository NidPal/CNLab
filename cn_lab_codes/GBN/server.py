import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 5002))
s.listen()
print('Listening on 5002 (Ctrl+C to stop)')
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
                    elif f > lost and lost >= start and lost < start + w:
                        lines.append(f'Frame {f} discarded (GBN)')
                    else:
                        lines.append(f'ACK {f}')
                if lost in frames:
                    lines.append(f"Timeout: resend frames {list(range(lost, min(start + w, n)))}")
                    for f in range(lost, min(start + w, n)):
                        lines.append(f'Resent {f} -> ACK {f}')
            c.sendall(('\n'.join(lines) + '\n').encode())
        except (ValueError, OSError) as e:
            c.sendall(('Error: ' + str(e)).encode())
