from socket import *
import datetime
import json
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL)

def recv_data():
        data = conn.recv(1024)
        #print("Received: ", repr(data))
        reply = "Received data"
        reply_enc = str.encode(reply)
        type(reply_enc)
        conn.sendall(reply_enc)
        return data


HOST = ''
PORT= 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by: ', addr)

while True:
        raw = recv_data()
        val = raw.decode()
        if len(val) != 0:
                logEntry = json.loads(val)
                print("Log Time: ", logEntry[0])
                print("PlateNo : ", logEntry[1])
                print("Entry   : ", logEntry[2])
        


#while True:
        #data = conn.recv(1024)
        #print("Received: ", repr(data))
        #reply = "Received data"
        #reply_enc = str.encode(reply)
        #type(reply_enc)
        #conn.sendall(reply_enc)

conn.close()
