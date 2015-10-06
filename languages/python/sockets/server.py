import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
l_onoff = 1
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, struct.pack('i', l_onoff))
host = '0.0.0.0'
port = 10000
s.bind((host, port))
backlog = 5
s.listen(backlog)
while 1:
    (clientsocket, address) = s.accept()
    print address
    clientsocket.send('server says: bye\n')
    clientsocket.close()

