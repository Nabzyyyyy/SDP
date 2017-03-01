import socket

HOST = '' #localhost
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) #how any connections it can receive at one time
#conn, addr = s.accept() # accept the conncetion
(client,(ip,port))=s.accept() #ADDED
print ('Connected by' , addr)  #prints address of connected node
i = True
while i is True:
	data = conn.recv(1024) #receives 1024 bytes of data using conn and stores into data
	print ("received ", repr(data)) #prints data 
	reply = raw_input('Reply: ')
	conn.sendall(reply)

conn.close()

