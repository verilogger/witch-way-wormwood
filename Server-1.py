""" Isa Abello
TCP Server

References:
https://pythontic.com/modules/socket/send
https://www.geeksforgeeks.org/socket-programming-python/
https://www.programiz.com/python-programming/exception-handling
https://docs.python.org/3/library/socket.html
https://docs.python.org/3/library/socketserver.html#module-socketserver
"""
#----- A simple TCP based server program in Python using send() function -----
import socket
import argparse
# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

# Bind and listen

serverIP = '127.0.0.1'

parser = argparse.ArgumentParser(
    prog='client.py',
    description='What the program does',
    epilog='text at the bottom of help'
)

parser.add_argument('--port')

args = parser.parse_args()

totalClients = 0



print("Server listening on", serverIP,':',int(args.port))

clients = []

clients = 0


# Accept connections

while True:
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((serverIP, int(args.port)))
    serverSocket.listen()

    (clientConnected, clientAddress) = serverSocket.accept()

    dataFromClient = clientConnected.recv(1024)
    decoded = (dataFromClient.decode())

    if 'REGISTER' in str(decoded):
        decodedList = (str(decoded)).split('\r\n')
        infoDict = dict()

        for i in decodedList:
            if ':' in i:
                tempList = i.split(':')
                infoDict.update({tempList[0]:tempList[1]})
            else:
                continue

        message = 'REGACK\r\nclientID: '+(infoDict['clientID'])+'\r\nIP: '+(infoDict['IP'])+'\r\nPort: '+(infoDict['Port'])+'\r\n\r\n'

        print(message)

        clientConnected.send(((message).encode()))

        clientConnected.close()

    elif 'BRIDGE' in str(decoded):
        if clients == 0:
            message = 'BRIDGEACK\r\nclientID: '+'\r\nIP: '+'\r\nPort: '+'\r\n\r\n'
            print(message)
            clientConnected.send(((message).encode()))
            clients+=1
        else:
            message = 'BRIDGEACK\r\nclientID: '+(infoDict['clientID'])+'\r\nIP: '+(infoDict['IP'])+'\r\nPort: '+((infoDict['Port']).strip(' '))+'\r\n\r\n'
            print(message)
            clientConnected.send(((message).encode()))