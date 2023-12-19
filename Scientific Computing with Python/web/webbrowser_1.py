import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode() converts from Unicode to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512) # 512 characters
    if (len(data) < 1):
        break
    print(data.decode()) # decode() converts from UTF-8 to Unicode
mysock.close()


