import socket

host='localhost'
port=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

filename='abc.txt'

sock.send(filename.encode())

readFile=sock.recv(1024)

print(readFile.decode())
sock.close()