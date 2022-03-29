import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 9000)

sock.connect(addr)
msg = sock.recv(1024)

print(msg.decode())
sock.send('DongHyeok Lee'.encode())

data = sock.recv(1024)
print(data.decode)
sock.close()