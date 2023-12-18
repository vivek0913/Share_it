import socket

host='localhost'
port=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(1)

print("The server is listening to clients requests")

conn, address = sock.accept()

print("connection has been established with",str(address))


try:
    
    fileName=conn.recv(1024)
    
    file=open(fileName,'rb')
    
    readFile=file.read()
    
    conn.send(readFile)
    
    file.close()

except:
    
    conn.send("File not found on the server.".encode())

conn.close()