import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
#ip_address = '192.168.43.42' #this one's is 160
port = 8000

sock.bind((ip_address, port)) #creates the following connection to the node at that ip using a specific port
sock.listen(2) #listens to this many clients
(client,(ip,port))=sock.accept()
