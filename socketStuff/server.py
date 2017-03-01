from socket import *

HOST = ''
PORT= 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by: ', addr)

while True:
        data = conn.recv(1024)
        print("Recieved: ", repr(data))
        reply = input("Reply: ")
        reply_enc = str.encode(reply)
        type(reply_enc)
        conn.sendall(reply_enc)

conn.close()
