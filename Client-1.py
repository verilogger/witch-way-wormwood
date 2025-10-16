""" Isa Abello
TCP Client

References:
https://pythontic.com/modules/socket/send
https://www.geeksforgeeks.org/socket-programming-python/
https://www.programiz.com/python-programming/exception-handling
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
https://docs.python.org/3/library/argparse.html
https://www.geeksforgeeks.org/python-assign-multiple-variables-with-list-values/
https://stackoverflow.com/questions/409783/socket-shutdown-vs-socket-close
"""

#----- A simple TCP client program in Python using send() function -----

import socket
import sys
import errno
import argparse

# Create a client socket

# client will have about 4 cmdl args
# 0 = program
# 1 = client id --id='student1'
# 2 = port number that client is listening --port=3000
# 3 = server ip address/port number --server-'200.26.180.43:5555'

# Connect to the server

# collect all args

# if any args are missing:
# 'insufficient amount of arguments.'

parser = argparse.ArgumentParser(
    prog='client.py',
    description='What the program does',
    epilog='text at the bottom of help'
)

parser.add_argument('--id')
parser.add_argument('--port')
parser.add_argument('--server')

args = parser.parse_args()

print(args.id, args.port, args.server)
splitServer = (str(args.server)).split(':')
serverIP, serverPort = splitServer[0], splitServer[1]

clientListening = str(args.port)

print(str(args.id),'running on',str(serverIP))

client1_Port = 0

wait = False

# Send data to server
while True:

    while True:
        data = input("")
        
        if data == '/id':
            print(str(args.id))
            data = ''
            continue

        elif data == '/register':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((serverIP,int(serverPort)))
            
            print("You are going to register by sending a REGISTER message to the server!")
            # "req type"
            msg1 = 'REGISTER\r\n'

            # "headers"
            msg2 = 'clientID: ' + str(args.id) + '\r\n'
            msg3 = 'IP: ' + str(serverIP) + '\r\n'
            msg4 = 'Port: ' + str(args.port) + '\r\n\r\n'
            clientSocket.send((msg1).encode())
            clientSocket.send((msg2).encode())
            clientSocket.send((msg3).encode())
            clientSocket.send((msg4).encode())

            dataFromServer = clientSocket.recv(1024)
            print(dataFromServer.decode())

            clientSocket.close()

            continue

        elif data == '/bridge':
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((serverIP,int(serverPort)))

            # req type
            msg5 = 'BRIDGE\r\nclientID: ' + str(args.id) + '\r\n\r\n'

            # sending
            clientSocket.send((msg5).encode())
            #clientSocket.send((msg6).encode())

            # receiving
            
            dataFromServer2 = clientSocket.recv(1024).decode()
            print(dataFromServer2)

            otherClientInfo = dataFromServer2.split('\r\n')

            for i in otherClientInfo:
                if 'clientID' in i:

                    otherClientIDsplit = (i.split(': '))
                    otherClient2ID = (otherClientIDsplit[1])

                    if otherClient2ID == '':
                        #empty headers
                        print('IN WAIT MODE')

                        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        clientSocket.bind(("127.0.0.1", int(args.port)))
                        clientSocket.listen()
                        conn, addr = clientSocket.accept()
                        
                        while True:
                            dataFromClient2 = conn.recv(1024)
                            print(dataFromClient2.decode())

                            if (dataFromClient2.decode()) == '/quit':
                                print("Client 1 received Client 2's request to shut down.\r\n")
                                clientSocket.shutdown(socket.SHUT_RDWR)
                                clientSocket.close()
                                exit()
                            
                            message = input('')

                            if message == '/id':
                                print(args.id)
                                continue

                            if message == '/quit':
                                quit = True
                                print("Client 1 wants to close the socket to Client 2.\r\n")
                                conn.send(((message).encode()))
                                exit()

                            else:
                                conn.send(((str(args.id)+'> '+message).encode()))
                                continue

                elif 'Port' in i:
                    client1_Port_Split = (i.split(': '))
                    client1_Port = (client1_Port_Split[1])

        elif data == '/chat':
            print("IN CHAT MODE")            
            client1_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client1_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print(client1_Port)
            client1_Socket.connect(('127.0.0.1', int(client1_Port)))

            while True:
                message = input('')

                if message == '/id':
                    print(args.id)
                    continue

                elif message == '/quit':
                    print("Client 2 is closing the socket to Client 1.\r\n")
                    client1_Socket.send(((message).encode()))
                    exit()

                else:
                    client1_Socket.send(((str(args.id)+'> '+message).encode()))

                    dataFromClient1 = client1_Socket.recv(1024)

                    if dataFromClient1.decode() == '/quit':
                        client1_Socket.shutdown(socket.SHUT_RDWR)
                        client1_Socket.close()
                        print("Shutting down the socket.\r\n")
                        exit()
                    
                    else:
                        print((dataFromClient1.decode()))
                        continue

        elif data == '/quit':
            print("Shutting down.\r\n")

            try:
                clientSocket.shutdown(socket.SHUT_RDWR)
            except:
                pass

            try:
                clientSocket.close()
            except:
                pass
            exit()
    
    if quit == True:
        print("Goodbye! The socket will close now.")
        try:
            clientSocket.shutdown(socket.SHUT_RDWR)
        except:
            pass
        clientSocket.close()
        exit()