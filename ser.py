import socket
import sys
import datetime
import threading

# status:
status_unsent=0
status_sent=1
ststus_receivedResponse=2
ststus_forwardedResponse=3

ArduinoClient=0
NormalClient=1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
<<<<<<< HEAD
server_address = ('', 80)
print('starting up on %s port %s' % (server_address[0],server_address[1]))
=======
server_address = ('localhost', 10002)
print('starting up on %s port %s', server_address[0],server_address[1])
>>>>>>> f5f98341bfd779edbf2cb1c460990d05303f7638
sock.bind(server_address)
sock.listen(1)
q = []

def query(q, id):
    for (t,i,s) in q:
        if i == id:
            return (t,s,i)

def insertAndAddTime(q, id, status):
    time = datetime.ctime()
    q.insert((time, id, status))
    return time

def change_status_to_sent(q, id, status):
    for (t,i,s) in q:
        if (t,i,s) == (time, id, status) and status == status_unsent:
            q.remove((time, id, status))
            q.insert((time, id, status_sent))
def change_status_to_received(q, id, status):
    for (t,i,s) in q:
        if (t,i,s) == (time, id, status) and status == status_sent:
            q.remove((time, id, status))
            q.insert((time, id, status_receivedResponse))

def notifyPhone():
    # TOBE ENABLED BY SWIFT
    pass

requestCount = 0;

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
<<<<<<< HEAD
            data = connection.recv(50)
            print ('received information: %s', data)
=======
            data = connection.recv(64)
            print ('received information:')
            print (len(data))

>>>>>>> 563cc75781b51c54c7a244c85a50e6a04c7435ed
            if data:
                # s = str(data).split("x")
                # print(s)
                if (str(data).count("\\")>10):
                    notifyPhone();
                    requestCount += 1;

                    if (requestCount > 8):
                        connection.sendall("ACCEPTED")
                    
#                 if len(s) != 3:
#                     print("Parse Failure: +")
#                 print(s)
#                 type = s[0]
#                 id = int(s[1])
#                 status = int(s[2])
#                 if type == "Pressed":
#                     time = insertAndAddTime(q, id, status)
#                     print('sending data back to the client')
#                     connection.sendall(time+"_"+str(id)+"_"+str(status))
#                     change_status_to_sent(q, id, status)
#                 if type == "Client":
#                     print(1)
# #                    if status == 1:
#                     connection.sendall("Received!")
#                     change_status_to_received(q, id, status)

<<<<<<< HEAD
            # else:
            print('no more data from %s:%s'% client_address)
            break
=======
            else:
                print('no more data from', client_address)
                break
>>>>>>> f5f98341bfd779edbf2cb1c460990d05303f7638
            
    finally:
        # Clean up the connection
        connection.close() 