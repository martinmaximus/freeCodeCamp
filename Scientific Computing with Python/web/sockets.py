import socket

mysock = socket.socket(socket.AF_INET, socket.Sock_STREAM)
mysock.connect(('data.pr4e.org', 80))
