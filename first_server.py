from asyncio.windows_utils import BUFSIZE
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    data = s.recv(1024)
    print(data.decode)

    s.send('20171501'.encode())
        
    client.close()